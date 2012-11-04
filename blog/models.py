from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()
    category = models.ManyToManyField("Category")

    def __unicode__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title
