from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import title


class Question(models.Model):

    STATUS_CHOICES = (
        ('draft' , 'Draft'),
        ('published' , 'Published')
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author_name = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_author_name")
    description = models.TextField()
    likes  = models.ManyToManyField(User, blank=True, related_name="user_likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image  = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.user.username

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_comment")
    description = models.TextField()
    created_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question.title},{self.user.username}"







