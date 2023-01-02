from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'username'


class Notes(models.Model):
     user=models.ForeignKey(User, on_delete=models.CASCADE)
     title=models.CharField(max_length=200)
     description=models.TextField()

     class Meta:
         verbose_name="notes"
         verbose_name_plural="notes"

     def __str__(self):
         return self.title


class Homework(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    description=models.TextField()
    due=models.DateTimeField()
    is_finished=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    is_finished=models.BooleanField(default=False)

    def __str__(self):
        return self.title

        


    