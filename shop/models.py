from django.db import models

Cameras_Photography = "Cameras & Photography"
Tv_Audio = "Tv & Audio"
SmartPhones_Tablets = "SmartPhones & Tablets"
Laptop_Computer = "Laptop & Computer"
Sony = "Sony"
Mobile = "Mobile"
Sports = "Sports"
Books = "Books"
Speaker = "Speaker"
All_categories = "All categories"

CATEGORIES = (
    (All_categories , "All categories"),
    (Cameras_Photography , "Cameras & Photography"),
    (Tv_Audio ,"Tv & Audio"),
    (SmartPhones_Tablets , "SmartPhones & Tablets"),
    (Laptop_Computer , "Laptop & Computer"),
    (Sony ,"Sony"),
    (Mobile , "Mobile"),
    (Sports , "Sports"),
    (Books , "Books"),
    (Speaker ,"Speaker")
)
class Goods(models.Model):
    name = models.CharField(verbose_name='Name',max_length=100)
    info = models.TextField(verbose_name='Info')
    image = models.ImageField(upload_to='media/',blank=True, verbose_name='image')
    current_price = models.FloatField(default=0,verbose_name='Current price')
    old_price = models.FloatField(default=0,verbose_name='Old Price')
    category = models.CharField(max_length=35,choices=CATEGORIES,default=All_categories)
    class Meta:
        pass
    def __str__(self):
        return self.name

class Photos(models.Model):
    image = models.ImageField(upload_to='media/',blank=True,verbose_name='image')
    location = models.ForeignKey('Goods', related_name='photos',on_delete=models.CASCADE)