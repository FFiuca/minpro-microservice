from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from man_user.view.login_view import LoginView, LogoutView


from man_user.view import register_view

app_name= 'man_user'

url_guest = [
    path('register/', include([
        path('admin/', register_view.RegisterAdminView.as_view(), name='register.admin'), # use genericView post method will hit create function and etc
        path('customer/', register_view.RegisterCustomerView.as_view(), name='register.customer')
    ])),
    path('auth/', include([
        path('login/', LoginView.as_view(), name='auth.login'),
        path('logout/', LogoutView.as_view(), name='auth.logout')
    ])),
]

url_user = [

]

urlpatterns = url_guest+ url_user
