from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.index,name="home"),
    path('login', views.loginuser,name="login"),
    path('logout', views.logoutuser,name="logout"),
    path('about', views.about,name="about"),
    path('products', views.products,name="products"),
     path('Potatochips', views.Potatochips,name="Potatochips"),
      path('TomatoKetchup', views.TomatoKetchup,name="TomatoKetchup"),
]
 