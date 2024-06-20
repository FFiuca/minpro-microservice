from django.contrib import admin
from django.urls import path, include
from uploader.views import UploadView

app_name= 'uploader'

url_guest = [

]

url_user = [
    path('upload/', UploadView.as_view({'post': 'upload'}), name='uploader|upload')
]

urlpatterns = url_guest+ url_user


