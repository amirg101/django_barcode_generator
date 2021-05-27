from django.shortcuts import render,redirect

# Create your views here.
from .models import Products
from .forms import ProductsForm

def index(request):
    productform=ProductsForm()
    if request.method=='POST':
        form=ProductsForm(request.POST)
        if form.is_valid():
            post=form.save()
            print(post.pk,post.Product_name)
            
            return redirect(f'barcode/{post.Product_name}/{post.pk}')
    return render(request,'index.html',{'form':productform})


def barcode(request,Product_name,pk):
    pro=Products.objects.filter(Product_name=Product_name,pk=pk)

    return render(request,'barcode.html',{'pro':pro})