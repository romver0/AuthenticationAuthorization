from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ауентификация
    path('signup/', views.signupuser, name='register'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    # Профиль пользовтеля
    # path('profile/', views.signupuser, name='register'),
    # Тудушки
    path('', views.home, name='home'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('game/',views.gameviews,name='game')
]