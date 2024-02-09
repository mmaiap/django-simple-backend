
from django.urls import include, path
from rest_framework import routers
from .views import *
from . import views

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
 

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_user, name='add-user'),
    path('user/view/<int:pk>/', views.view_user, name='view-user'),
    path('all/', views.view_users, name='view-users'),
]