from django.urls import path
from . import views


urlpatterns=[
    path('employee/<str:pk1>',views.tasks, name='dashboard'),
    path('register/', views.registerPage, name="register"),
    path('profile/<str:pk>',views.profile, name='profile'),
    path('delete/<str:pk>/',views.deleteTask, name='del-task'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('adminer/',views.adminpage, name='admin'),
    path('export_csv/<str:pk1>',views.export, name='export'),
    path('welcome/',views.welcome,name="welcome")

]