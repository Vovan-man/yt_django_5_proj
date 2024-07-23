from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.

def index(request):
    items = Product.objects.all() 
    context = {
        'items':items
    }                                                          #["Iphone", "Xiomi", "Samsung"]
    return render(request, "myapp/index.html", context)            #return HttpResponse(items) 


def indexItem(request, my_id):
    item = Product.objects.get(id=my_id)
    context = {
        'item':item
    }
    return render(request, "myapp/detail.html", context=context)


#def contacts(request):
   # return render(request, "myapp/contacts.html")         # HttpResponse("<h1>Это наши контакты:</h1>")
