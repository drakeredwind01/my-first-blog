from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='base'),
    path('resume/', views.resume, name='resume'),
]