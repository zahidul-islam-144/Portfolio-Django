from . import views
from django.urls import path

app_name = 'App_Core'

urlpatterns = [
    path('home/', views.homePage, name=''),
    # path('login/', views.loginPage, name=''),
]