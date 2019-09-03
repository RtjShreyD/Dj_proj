from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #Importing user who will be authors, users are a different table created by Django 

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #if date is not added by user posting then it will take current default date
    author = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete=....here is specifying if the user is deleted then delete the posts too
    
    #For making the post object more descriptive(while calling) we create a dunder(___) function
    def __str__(self):
        return self.title
