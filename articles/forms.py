from django import forms
from .models import Article, Comment
from .validators import title_validate
from django.core.exceptions import ValidationError


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '제목을 입력하세요'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '내용을 입력하세요',
                    'rows': 5,
                }
            )
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        title_validate(title)
        return title

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)