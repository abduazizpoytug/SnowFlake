from django.db import models

class Home(models.Model):
    
    login = models.CharField(max_length=80)
    
    def __str__(self):
        return self.logo