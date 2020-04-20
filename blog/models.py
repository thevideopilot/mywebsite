from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Resume(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    task = models.TextField()
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.role


class About(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    email = models.EmailField()
    number = models.CharField(max_length=11)
    github = models.URLField()
    linkdeln = models.URLField()
    twitter = models.URLField()
    bio = models.TextField()
    skills = models.TextField()
    hobbies = models.TextField()


    def __str__(self):
        return f'{self.user.get_full_name()} Profile'

    def save(self):
        super().save()