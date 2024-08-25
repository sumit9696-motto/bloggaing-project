from django.urls import path
from . import views


urlpatterns=[
    path('', views.home),
    path('home/', views.home),
    path('aboutus/', views.aboutus),
    path('contactus/', views.contactus),
    path('createblogs/', views.createblogs),
    path('latestblogs/', views.latestblogs),
    path('myblogs/', views.myblogs),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('logout/', views.logout),

]