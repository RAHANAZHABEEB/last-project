from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('top/',views.top,name='top'),
    path('dreamy/',views.dreamy,name='dreamy'),
    path('signup/',views.signup,name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="user_logout"),
]
