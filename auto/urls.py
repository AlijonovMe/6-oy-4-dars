from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('brands/<int:pk>/', brands, name='brand_detail')
]