from django.db import models

# Create your models here.
class UserAuth(models.Model):
    userid = models.IntegerField('User_id', default=1000)
    username = models.CharField('Username', max_length=50)
    password = models.CharField('Password', max_length=50)
    
    def __str__(self):
        return self.username