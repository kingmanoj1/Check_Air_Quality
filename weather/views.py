from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib import auth
import requests
import urllib.request
from bs4 import BeautifulSoup
from django.http import JsonResponse

# Create your views here.

def about(request):
    try:
       
        page = requests.get('http://aqicn.org/scale')
    
        soup = BeautifulSoup(page.text, 'html.parser')
        #p1=soup.prettify()
        zero=soup.find_all('table')[2]
      
        
        return render(request,'weather/about.html',{"zero":zero})

    except:
        return render(request,'error404.html')

def show(request):
       
            data=request.POST
            token="b272f7c902ad48302642e380dc7b4f5614915308"
            city=str(data.get("ci"))
            
            url="https://api.waqi.info/feed/"+city+"/?token="+token
            data=requests.get(url).json()
            #return JsonResponse({"data":data})

            

            return render(request,'weather/show.html',{"data":data,
            'city':city,
            
            
            })
            
        
def search(request):
    return render(request,'weather/home.html')

