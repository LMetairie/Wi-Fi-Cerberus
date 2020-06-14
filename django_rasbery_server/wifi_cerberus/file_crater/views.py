from django.shortcuts import render
from django.http import  HttpResponseRedirect, HttpResponse
from django.urls import reverse
from os import walk
from django.conf import settings

# Create your views here.
def captures_list(request):
    
    file_list = []

    for files in walk(getattr(settings, 'BASE_DIR', None)+'/media/wireless_captures/'):
        for filename in files:
            file_list.append(filename)
    
    context = {'file_list':file_list}
    return render(request, 'captures_list.html', context)

def getFile(requst, num):
    
    return 