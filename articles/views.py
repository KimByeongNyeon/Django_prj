from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

# Article List (Index)
class ArticleListView(ListView):
    model = Article
    template_name = 'articles/index.html'
    context_object_name = 'articles'

# Article Detail
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments_form'] = CommentForm()
        context['comments'] = self.object.comment_set.all()
        return context

# Article Create
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/new.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # 로그인한 사용자로 설정
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('articles:detail', kwargs={'pk': self.object.pk})

# Article Update
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/edit.html'

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.user  # 작성자 본인만 수정 가능

    def get_success_url(self):
        return reverse_lazy('articles:detail', kwargs={'pk': self.object.pk})

# Article Delete
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'articles/confirm_delete.html'
    success_url = reverse_lazy('articles:index')

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.user  # 작성자 본인만 삭제 가능

# Comment Create
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', pk=pk)

# Comment Delete
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'articles/confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user  # 댓글 작성자 본인만 삭제 가능

    def get_success_url(self):
        article_pk = self.object.article.pk
        return reverse_lazy('articles:detail', kwargs={'pk': article_pk})

# Article Like Toggle
class LikeToggleView(LoginRequiredMixin, View):
    def post(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        if request.user in article.like_users.all():
            article.like_users.remove(request.user)  # 좋아요 취소
        else:
            article.like_users.add(request.user)  # 좋아요 추가
        return redirect('articles:index')
