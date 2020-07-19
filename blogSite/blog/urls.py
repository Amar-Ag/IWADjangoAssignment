from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.homePage, name='home'),
    path('<slug:slug>/', views.BlogsDetail.as_view(), name='detail'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
    path('blogs/', views.BlogsList.as_view(), name='blogs'),

]
