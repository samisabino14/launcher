from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class UserData(AbstractBaseUser):

    # custom User models must have an integer PK
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['username']

        def __unicode__(self):
            return self.username

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

        def __unicode__(self):
            return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    author = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.title} {self.content} {self.category.name}'

    def get_absolute_url(self):
        return reverse('detalhe_do_post_do_blog', args=[self.slug, ])

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_at']

        def __unicode__(self):
            return self.title


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

        def __unicode__(self):
            return self.content
