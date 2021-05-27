from django import forms
from .models import Products
class ProductsForm(forms.ModelForm):
    class Meta:
        model=Products
        fields=['Product_name','country_id','manufacturer_id','number_id']    