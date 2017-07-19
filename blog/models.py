from django.db import models
#使用ORM框架
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
