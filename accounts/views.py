from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login as auth_login, update_session_auth_hash
from .forms import CustomUserCreationForm, CustomChangeForm
from django.shortcuts import redirect

User = get_user_model()

# 로그인 뷰
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('articles:index')


# 로그아웃 뷰
class UserLogoutView(LogoutView):
    next_page = 'articles:index'


# 회원가입 뷰
class SignupView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('articles:index')


# 회원 정보 수정 뷰
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomChangeForm
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('articles:index')

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)  # 세션 업데이트
        return super().form_valid(form)


# 회원 탈퇴 뷰
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/user_confirm_delete.html'
    success_url = reverse_lazy('accounts:logout')

    def get_object(self, queryset=None):
        return self.request.user


# 비밀번호 변경 뷰
class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('articles:index')

    def form_valid(self, form):
        form.save()
        # 세션 업데이트
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)
