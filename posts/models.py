from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(blank=False, max_length=200)
    content = models.CharField(blank=False, max_length=1500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(blank=False)
    is_modified = models.BooleanField(default=False)
    last_modified_on = models.DateTimeField(blank=False)
    numberofcomments = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return (self.title + '\n' + self.content + '\n')
    def get_absolute_url(self):
        return reverse('posts:list')

    # @property
    # def is_modified(self):
    #     return self.last_modified_on > self.created_on
    # not working

    # def get_absolute_url(self):
        # return reverse('posts:detail', kwargs={'pk':self.pk})
class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(blank=False, max_length=500)
    created_on = models.DateTimeField(blank=False)

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk':self.post_id.id})
