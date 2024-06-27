from django.db import models
# Create your models here.

import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uid= models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now_add=True)


    class Meta:
        abstract= True





class Blog(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title= models.CharField(max_length=500)
    blog_text= models.TextField()

    def __str__(self) -> str:
        return self.title   