from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=400)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.content
