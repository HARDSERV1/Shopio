from django.db import models

class Goods(models.Model):
    name = models.CharField(verbose_name='Name',max_length=100)
    info = models.TextField(verbose_name='Info')
    image = models.ImageField(upload_to='media/', verbose_name='image')

