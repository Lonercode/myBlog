# Generated by Django 4.2.10 on 2024-02-07 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0005_posts_imageinpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
