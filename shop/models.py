from django.db import models

class Goods(models.Model):
    name = models.CharField(verbose_name='Name',max_length=100)
    info = models.TextField(verbose_name='Info')
    image = models.ImageField(upload_to='media/',blank=True, verbose_name='image')
    current_price = models.FloatField(default=0,verbose_name='Current price')
    old_price = models.FloatField(default=0,verbose_name='Old Price')
    class Meta:
        pass
