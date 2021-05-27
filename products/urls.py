from django.urls import path,include
from .views import index,barcode
app_name="app"
urlpatterns = [
    path("",index,name="index"),
    path("barcode/<str:Product_name>/<int:pk>/",barcode,name="barcode"),


]