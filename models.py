from django.db import models
from django.shortcuts import render
from django.contrib.contenttypes.fields import GenericRelation
from tags.models import Tag, TaggedItem


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=Post.STATUS_PUBLISHED)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()


class Category(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_DRAFT = 'D'
    STATUS_PUBLISHED = 'P'
    STATUS_REJECTED = 'R'
    STATUS = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_REJECTED, 'Rejected'),
    )
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', through='PostCategories')
    tags = GenericRelation(TaggedItem)
    status = models.CharField(
        choices=STATUS,
        default=STATUS_DRAFT,
        max_length=2
    )
    objects = PostManager()

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title


class PostCategories(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)
