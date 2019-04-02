from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model

import misaka

from groups.models import Group

User = get_user_model()

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name = 'posts', on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now = True)
    message = models.TextField()
    message_html = models.TextField(editable = False)
    group = models.ForeignKey(Group, related_name = 'posts', on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs = {'pk': self.pk, 'username': self.user.username})
    
    class Meta:
        ordering = ['-created_date']
        unique_together = ['user', 'message']
