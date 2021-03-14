from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TODO(models.Model):
    
    status_choices = [
        ('C', 'COMPLETED'),
        ('P', 'PENDING'),
    ]

    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2 , choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey( User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title 