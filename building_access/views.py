from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Contact
from .models import Tag




def home(request):
    context = {
        'products': Product.objects.all(),
        'contact': Contact.objects.all(),
        #'groups': Group.objects.all(),
        #'phone' : Phone.objects.all(),
        'tags' : Tag.objects.all
    }
    
    return render(request, 'tag/home.html', context)


def about (request):
    return render(request, 'tag/about.html', {'title': 'About'})
