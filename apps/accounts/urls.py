from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
]
