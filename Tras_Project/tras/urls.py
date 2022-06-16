from os import name
from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.index, name = "index"),
    path('footer/',views.index_1,name="footer"),
    path('main/', views.main,name="main"),
    path('acticle_page/', views.acticle, name="acticle_page")
]