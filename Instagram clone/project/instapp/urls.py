"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .import views



urlpatterns = [
        path('', views.home, name="home"),
        path('logindone', views.logindone, name="logindone"),
        path('signup', views.signup, name="signup"),
        
        path('registerdone', views.registerdone, name="registerdone"),
        path('profileshow', views.profileshow, name="profileshow"),
        path('editprofile', views.editprofile, name="editprofile"),
        path('editeprofiledone', views.editeprofiledone, name="editeprofiledone"),
        path('search', views.search, name="search"),
        path('followounfollow', views.followounfollow, name="followounfollow"),
        
        
        
        
        
        
        


]

