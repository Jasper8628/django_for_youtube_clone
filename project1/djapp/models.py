from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(default="hi",max_length=120)
    content=models.TextField()
    
    def __str__(self):
        return self.title
    
class Book(models.Model):
    selfLink = models.TextField()
    title    = models.TextField()
    authors  = models.TextField()
    thumbnail= models.TextField()
    description=models.TextField()
    
    def __str__(self):
        return self.title