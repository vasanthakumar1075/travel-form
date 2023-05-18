from django.contrib import admin
from django.urls import path
from travelapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.register, name='api-register'),
    path('api/lists/', views.lists, name='api-lists'),
    path('', views.Register, name='register'),
    path('lists/', views.Lists, name='lists'),
]
