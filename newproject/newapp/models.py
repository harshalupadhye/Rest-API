from django.db import models

# Create your models here.
class boot(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)
    def __str__(self):
        return self.Email
      
