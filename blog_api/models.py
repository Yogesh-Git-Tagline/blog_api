from django.db import models
from django.contrib.auth.models import User


class BlogDate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Blog(BlogDate):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blogs')
    content = models.TextField()

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
