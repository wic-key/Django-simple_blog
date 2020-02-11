from django.urls import path,include
from .import views

urlpatterns = [
        path('',views.home,name="home"),
        path('register/',views.register,name='register'),
        path('login/',views.login,name='login'),
        path('logout/',views.logout,name='logout'),
        path('getstart/',views.getstart,name='getstart'),
        path('api/',views.index),
        path('registration_api/',views.registration_view,name='registration_api')
]