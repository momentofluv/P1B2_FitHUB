# Generated by Django 4.2 on 2024-08-15 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_article_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='community.article'),
        ),
    ]
