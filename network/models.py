from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    content = models.CharField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Post{self.id} made by {self.author} ON {self.date}"


class follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    
    def __str__(self) -> str:
        return 

