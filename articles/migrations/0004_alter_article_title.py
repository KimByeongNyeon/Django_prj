# Generated by Django 4.2.16 on 2024-10-02 00:31

import articles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_created_at_article_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=20, validators=[articles.validators.title_validate]),
        ),
    ]
