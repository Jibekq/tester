from django.db import models



class Post(models.Model):
    header = models.CharField(max_length=50)
    heading = models.TextField(max_length=1000)



   