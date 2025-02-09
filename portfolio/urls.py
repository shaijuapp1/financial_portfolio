# portfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('upload/', views.upload_portfolio, name='upload_portfolio'),
    path('signup/', views.signup, name='signup'),
]