from django.contrib import admin
from django.urls import path
from . import views

# route = routers.SimpleRouter()
# route.register('element',ElementViewSet)
# route.register('category',CategoryViewSet)
# route.register('type',TypeViewSet)

urlpatterns = [
    path('', views.index, name='index'),
]