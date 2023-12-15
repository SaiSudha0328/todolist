from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    #path('pk',views.updateTask, name="update_task")
    path('update_task/<str:pk>/', views.updatetask, name="update_task"),
    path('delete/<str:pk>/', views.deletetask, name="delete")
    #path('', views.index,name='index'),
    #path('submit',views.submit,name='submit')
    ]