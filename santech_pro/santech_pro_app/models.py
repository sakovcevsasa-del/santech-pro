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

    santehnick_tupe = (
        ('туалет', 'туалет'),
        ('сантехника', 'сантехника') 
    ) 

    item_title = models.CharField(max_length=100) # название товара
    price = models.FloatField() # цена
    description = models.CharField(max_length = 300) # описание 
    material = models.CharField(max_length=20) # материал
    proizvodstvo = models.CharField(max_length = 50) #  поизводство
    ves = models.FloatField() # вес товара
    tsvet = models.CharField(max_length = 20) # цвет товара
    santehnick_tupe = models.CharField(max_length = 20, choices=santehnick_tupe)
    dlina = models.FloatField() # длинна товара
    shirina = models.FloatField() # ширина товара
    visota = models.FloatField() # высота товара
    photo = models.ImageField() # фото товара

    def __str__(self):
        return f'{self.id}. {self.item_title}'


    #IntegerField() цело численный
    #FloatField() дробные
    #CharField() символьный
    #TextField() текстовый

