from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('add_user',views.Add_user ,name='add_user'),
    path('add_task',views.Add_task,name='add_task'),
    path('export_users_tasks_xls', views.export_users_xls, name='export_users_tasks_xls'),
    path('cus_login', views.custom_login, name='cus_login'),
    path('logout', views.logout_user, name='logout'),
]
