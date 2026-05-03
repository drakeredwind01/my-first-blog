from django.urls import path
from . import views

urlpatterns = [
    path('multiple_stopwatch', views.multiple_stopwatch, name='multiple_stopwatch'),
    path('stopwatches/', views.stopwatches, name='stopwatches'),
]
