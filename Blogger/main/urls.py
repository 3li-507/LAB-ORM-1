from django.urls import path
from . import views

app_name="main"
 
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('add/', views.add_post_view, name='add_post_view'),
    path('details/<int:poster_id>/', views.detail_post_view, name='detail_post_view'),
    path('update/<int:poster_id>/', views.update_post_view, name='update_post_view'),  
    path('delete/<int:poster_id>/', views.delete_post_view, name='delete_post_view'),
]