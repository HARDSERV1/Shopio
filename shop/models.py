from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=35)
    sub_category = models.ManyToManyField('Subcategory')

    class Meta:
        pass

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=35)

    class Meta:
        pass

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    info = models.TextField(verbose_name='Info')
    image = models.ImageField(upload_to='media/', blank=True, verbose_name='image')
    current_price = models.FloatField(default=0, verbose_name='Current price')
    old_price = models.FloatField(default=0, verbose_name='Old Price')
    category = models.ForeignKey('Category', default='All categories', null=True, on_delete=models.SET_NULL)
    sub_category = models.ForeignKey('Subcategory', default='', null=True, on_delete=models.SET_NULL)

    class Meta:
        pass

    def __str__(self):
        return self.name


class Photos(models.Model):
    small_image = models.ImageField(upload_to='media/', blank=True, verbose_name='small image')
    big_image = models.ImageField(upload_to='media/', blank=True, verbose_name='big image')
    location = models.ForeignKey('Goods', related_name='photos', on_delete=models.CASCADE)