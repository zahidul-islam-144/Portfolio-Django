from . import views
from django.urls import path

app_name = 'App_Edu'

urlpatterns = [
    path('about/', views.aboutPage, name=''),
]