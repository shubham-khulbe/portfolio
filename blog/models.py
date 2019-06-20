from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/')
    summary = models.TextField()
    date_pub = models.DateField()

    def time(self):
        return self.date_pub.strftime("%d %b %Y")

    def __str__(self):
        return self.title

    def summary_length(self):
        return (self.summary[:100] + "...")
