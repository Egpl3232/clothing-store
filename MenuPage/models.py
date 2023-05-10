from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=150)

    def __str__(self):
        return "%s %s" % (self.email, self.name)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'