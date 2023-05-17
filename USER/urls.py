from django.urls import path
from .views import HomeView
from . import views
urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('update/<str:pk>/',  views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),

]
