from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path("home/",views.home,name="home"),
    path("registration/",views.registration,name="registration"),
    path("login/",views.login,name="login"),
    path("course/",views.course,name='course'),
    path("dashboard/",views.dashboard,name='dashboard'),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("profile/",views.profile,name="profile"),
    path("logout/",views.logout,name='logout')

]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.STATIC_ROOT)