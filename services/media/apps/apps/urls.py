from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from uploader import urls as url_uploader

url_guest = [
    path('uploader/', include(url_uploader.url_guest))
]

url_user = [
    path('uploader/', include(url_uploader.url_user))
]


urlpatterns = [
    path('admin/', admin.site.urls),

    # apps
    path('media/', include([
        path('guest/', include(url_guest)),
        path('user/', include(url_user)),
    ])),

    # third
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.TESTING:
    urlpatterns+= [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
