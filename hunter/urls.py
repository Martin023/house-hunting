from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ,name='homepage'),
    path('gallery/',views.all_houses ,name='gallery'),
    path('house/<pk>/',views.get_house,name="gethouse"),
    path('add_house/',views.add_house,name='addhouse'),
    path('house/<pk>/edit/',views.update_house,name='update_house'),
    path('house/<pk>/delete',views.delete_house,name='delete'),
    path('register/', views.register, name="register"),
    path("login/", views.login_request, name="login"),
 
    path("logout/", views.logout_request, name= "logout"),
]