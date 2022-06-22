from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ,'homepage'),
    path('house/<pk>',views.get_house,name="gethouse"),
    path('add_house/',views.add_house,name='addhouse')
]