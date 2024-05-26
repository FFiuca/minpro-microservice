"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

url_guest = [
    path('man_user/', include('man_user.urls')),
    path('coba/', include('coba.urls')),
    path('/', include('coba.urls')),
    path('', include('coba.urls'))
]

url_user = [
    path('', include('coba.urls')),
    path('coba/', include('coba.urls')),
]

urlpatterns = [
    # system
    path('admin/', admin.site.urls),

    # apps
    path('man_user/', include([
        path('guest/', include(url_guest)),
        path('user/', include(url_user)),
    ])),

    # third
    path("__debug__/", include("debug_toolbar.urls")),

]
