from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(config_name='ckeditor')
    created = models.DateTimeField()
    categories = models.ManyToManyField("Category")
    tags = TaggableManager()
    slug = AutoSlugField(populate_from="title")
    published = models.BooleanField()

    def get_categories(self):
        return " | ".join([s.name for s in self.categories.all()])
    get_categories.short_description = "Categories"

    def is_published(self):
        return self.published
    is_published.boolean = True

    def __unicode__(self):
        return self.title
