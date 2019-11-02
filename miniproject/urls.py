from django.contrib import admin
from django.urls import path
import weather.views 
import contact.views
import feedback.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',weather.views.about,name="about"),
    path('show/',weather.views.show,name="show"),

    path('contact/',contact.views.contact,name="contact"),
    


    path('search/',weather.views.search,name="search"),

    path('feedback/',feedback.views.feedback,name="feedback"), 
    ]
