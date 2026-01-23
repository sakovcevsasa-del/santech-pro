import os
from django.db import models
from django.conf import settings

# CharField - текстовое поле
# IntegerField - целочисленное поле
# FloatField - дробное поле
# DateField - поле даты

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "images")

def item_description_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "item_descriptions")

class Item(models.Model):
    item_title = models.CharField(max_length=100) #название товара
    price = models.IntegerField() #цена
    description = models.FilePathField(path=item_description_path) #описание 
    material = models.CharField(max_length=20) #материал

