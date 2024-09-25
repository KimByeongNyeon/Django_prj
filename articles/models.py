from django.db import models
from .validators import title_validate
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20, validators=[title_validate])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
