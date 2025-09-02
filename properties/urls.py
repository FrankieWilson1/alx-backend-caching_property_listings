from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/properties/', views.property_list, name='property_list_api'),
]
