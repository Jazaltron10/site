from django.urls import path
from . import views

urlpatterns = [
    path('create_data/', views.create_data, name='create_data'),
    path('rockstar_games/', views.list_rockstar_games, name='list_rockstar_games'),
    path('update_gta_sales/', views.update_gta_sales, name='update_gta_sales'),
    path('delete_last_of_us/', views.delete_last_of_us, name='delete_last_of_us'),
    path('', views.home, name='home'),
]
