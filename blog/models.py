from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/')
    summary = models.TextField()
    date_pub = models.DateTimeField()
