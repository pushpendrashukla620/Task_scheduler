from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class User(models.Model):
    email = models.EmailField(validators=[EmailValidator()],blank=False,null=False,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

