from django.contrib import admin
from django.urls import path
from . import views
# this is url file
urlpatterns = [
    path('', views.home,name = 'home'),
    path('main', views.main,name = 'main'),
    path('add', views.add,name = 'add'),
    path('delete-todo/<int:id>', views.delete_todo,name = 'delete-todo'),
    path('change-status/<int:id>/<str:status>', views.change_status,name = 'change-status'),
]