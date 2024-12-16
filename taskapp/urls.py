from django.urls import path
from .views import category, rfx, home

urlpatterns = [
    path('', home, name='home'),
    path('category', category, name='home'),
    path('rfx', rfx, name='rfx'),
    # path('')
]
