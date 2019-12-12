from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('update_task/<int:pk>/',views.updateTask,name='update_task'),
    path('delete/<int:pk>/',views.deleteTask,name="delete")
]