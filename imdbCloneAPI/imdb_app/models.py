from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name