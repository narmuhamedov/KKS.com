from django.db import models


class Slider(models.Model):
    slides = models.URLField()

    def __str__(self):
        return self.slides

    class Meta:
        verbose_name = 'слайд'
        verbose_name_plural = 'слайды'


class Motto(models.Model):
    text = models.CharField(max_length=250)
    video_url = models.URLField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'девиз'
        verbose_name_plural = 'девизы'


class Contact(models.Model):
    adress = models.CharField(max_length=100)
    email = models.EmailField(default="@gmail.com", blank=True)
    phone_number = models.CharField(max_length=16)
    map = models.URLField()

    def __str__(self):
        return self.adress

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


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

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
