from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('top/',views.top,name='top'),
    path('dreamy/',views.dreamy,name='dreamy'),
    path('signup/',views.signup,name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('details/<int:id>/', views.details, name="details"),
    path('chick/',views.chick,name='chick'),
    path('about/',views.about,name="about"),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
