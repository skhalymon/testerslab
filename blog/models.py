from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()
    categories = models.ManyToManyField("Category")
    published = models.BooleanField()

    def get_categories(self):
        return " | ".join([s.name for s in self.categories.all()])
    get_categories.short_description = "Categories"

    def is_published(self):
        return self.published

    def __unicode__(self):
        return self.title
