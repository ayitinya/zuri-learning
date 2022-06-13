from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    Title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.author = self.request.user
        super(Post, self).save(*args, **kwargs)
