from django.shortcuts import render ,HttpResponse
from shop101.models import Product

# Create your views here.
def test(request):
    return HttpResponse('hello world')

def products_list(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'products_list.html', \
         context={'product_list': products})

def show_product(request,id):
        p_id=id
        product= Product.objects.get(id=p_id)
        return render(request,'show.html',context={'product':product})