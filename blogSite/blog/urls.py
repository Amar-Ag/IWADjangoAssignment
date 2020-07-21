from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogsList.as_view(), name='home'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
    path('<slug:slug>/', views.BlogsDetail.as_view(), name='detail'),
]
