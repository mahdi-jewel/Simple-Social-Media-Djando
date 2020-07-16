from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit_profile, name='edit'),
    path('user/<username>/', views.user, name='user'),
    path('follow/<username>/', views.follow, name='follow'),
    path('unfollow/<username>/', views.unfollow, name='unfollow'),
    
]
