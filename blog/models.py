from email.policy import default
from django.db import models
from tinymce import models as tinymce_models
from tinymce.models import HTMLField


class Post(models.Model):
    image = models.ImageField(upload_to='images', default='image')
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = tinymce_models.HTMLField()
    body = HTMLField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
