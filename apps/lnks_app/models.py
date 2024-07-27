from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    original_url=models.URLField(max_length=600)
    short_code=models.CharField(max_length=15,blank=True,null=True,unique=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self) -> str:
        return self.short_code or '---'
    

class Click(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.ForeignKey(Link,on_delete=models.SET_NULL,blank=True,null=True,related_name='clicks')
