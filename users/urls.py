'''Defines URL patterns for users_app'''

from django.urls import path
from django.contrib.auth.views import LoginView


from users import views

app_name='users'

urlpatterns = [
    #login page

    path('login/',LoginView.as_view(),name='login'),
    # path('login/',views.loign,name='login')
    #Logout page. 

    path('logout/',views.logout_view,name='logout'),

    #Registration Page
    path('register/',views.register,name='register'),


]