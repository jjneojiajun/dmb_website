from django.db import models


# Create your models here.
# Create your models here.
class blogPosts(models.Model):
    """Model to key in the rates of the bank"""
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title