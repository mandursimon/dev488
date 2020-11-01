from django.shortcuts import render
from django.http import HttpResponse




def home(request):
    context = {
        #'tags': Tag.objects.all(),
        #'doors': Door.objects.all(),
        #'groups': Group.objects.all(),
        #'phone' : Phone.objects.all(),
    }
    
    return render(request, 'tag/home.html', context)


def about (request):
    return render(request, 'tag/about.html', {'title': 'About'})
