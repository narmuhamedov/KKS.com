from django.db import models


class About(models.Model):
    text = models.TextField()
    logo = models.ImageField()

    def __str__(self):
        return self.text



class BlogTable(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    instagram = models.URLField()
    music = models.FileField(upload_to='music/', null=True)
    price = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-{self.created_at}'
