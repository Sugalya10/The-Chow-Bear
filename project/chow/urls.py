from django.urls import path
from chow import views
from chow.views import *

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('menu',views.fare,name="menu"),
    path('menu/<str:name>',views.menucard,name="menu"),
    path('menu/<str:sname>/<str:dname>',views.dishlist,name="dishlist"),
    path('custom',views.custom,name="custom"),

]
