from django.contrib import admin
from django.urls import path
# from .views import index, about
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
]
