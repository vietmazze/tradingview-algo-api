from django.db import models


# Create your models here.
class Alert(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='alert', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title