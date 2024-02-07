from django.db import models

# Create your models here.

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/')
    imageInPage = models.ImageField(upload_to='images/')
    title =models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title