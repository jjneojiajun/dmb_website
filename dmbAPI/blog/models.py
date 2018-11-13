from django.db import models


# Create your models here.
# Create your models here.
class blogPosts(models.Model):
    """Model to key in the rates of the bank"""
    name = models.CharField(max_length=109, blank=False, default='')
    content = models.TextField(max_length=10000, blank=False, default='')

    def __str__(self):
        return self.name