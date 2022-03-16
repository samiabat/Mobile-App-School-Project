from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes),
    path('wiget/', views.getWidgets),
    path('apps/', views.getApps),
    path('apps/create/', views.createApp),
    path('apps/delete/<str:pk>/', views.deleteApp),
    path('apps/update/<str:pk>/', views.updateApp),
    path('apps/<str:pk>/', views.getApp),
]