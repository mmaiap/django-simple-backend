
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
]