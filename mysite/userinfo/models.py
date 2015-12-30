from django.db import models
from validation.models import UserAuth

# Create your models here.
class Tag(models.Model):
    name = models.CharField('TagName', max_length=50, null=True)
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    blog_title = models.CharField('BlogTitle', max_length=80)
    blog_body = models.TextField('BlogBody', max_length=5000)
    blog_tags = models.ManyToManyField(Tag)
    blog_read_count = models.IntegerField('BlogReadCount', default=0, null=True)
    blog_votes = models.IntegerField('BlogVotes', default=0, null=True)
    blog_publish_date = models.DateTimeField('BlogPublishDate', auto_now_add=True)
    blog_modify_date = models.DateTimeField('BlogPublishDate', auto_now=True)
    
    def __str__(self):
        return self.blog_title
    
class Name(models.Model):
    lastname = models.CharField('LastName', max_length=50, null=True)
    firstname = models.CharField('FirstName', max_length=50, null=True)
    promisewords = models.CharField('FirstName', max_length=50, null=True)
    
    def __str__(self):
        return self.lastname
    
class Info(models.Model):
    user = models.ForeignKey(UserAuth, null=True)
    name = models.ForeignKey(Name, null=True)
    blogs = models.ManyToManyField(Blog)
    
class Test(models.Model):
    kindof=models.CharField('KindOf', max_length=50)
    tags = models.ManyToManyField(Tag)