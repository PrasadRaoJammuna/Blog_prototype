
from .views import post_detail,blog_post,post_create,post_update,delete_post,dashboard
from django.urls import path 

urlpatterns = [
    path('',blog_post,name='blog'),
    path('post_detail/<str:slug>/',post_detail,name='post_detail'),
    path('create_new/',post_create,name='create_new'),
    path('update/<str:slug>/',post_update,name='post_update'),
    path('delete/<str:slug>/',delete_post,name='delete_post'),
    path('dashboard/',dashboard,name='dashboard')


]



