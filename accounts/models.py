from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    auth_token = models.CharField(max_length=500)
    is_verified = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
class ResetPassword(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=500)
    is_used = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
        