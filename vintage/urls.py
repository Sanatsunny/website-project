from django.urls import path
from . import views
urlpatterns=[
    path("home/",views.home,name="home"),
    path("registration/",views.registration,name="registration"),
    path("login/",views.login,name="login"),
    path("course/",views.course,name='course'),
    path("dashboard/",views.dashboard,name='dashboard')
]