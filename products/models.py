from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
# Create your models here.
class Products(models.Model):
    Product_name=models.CharField(max_length=200)
    barcode=models.ImageField(upload_to='images/',blank=True)
    country_id=models.CharField(max_length=1,null=True)
    manufacturer_id=models.CharField(max_length=6,null=True)
    number_id=models.CharField(max_length=5,null=True)
    


    def __str__(self):
        return str(self.Product_name)

    def save(self,*args,**kwargs):
        EAN=barcode.get_barcode_class('ean13')
        ean=EAN(f'{self.country_id}{self.manufacturer_id}{self.number_id}',writer=ImageWriter())
        buffer=BytesIO()
        ean.write(buffer)
        self.barcode.save(f'{self.Product_name}.png',File(buffer),save=False)
        return super().save(*args,**kwargs)