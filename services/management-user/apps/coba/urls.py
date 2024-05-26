from django.urls import path, include
from . import views

app_name='coba'
urlpatterns = [
    path('test1/', views.Test.as_view(), name='test1'),
    path('', views.Test.as_view(), name='test2'),
]

