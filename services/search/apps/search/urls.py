from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from search.views import SearchView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny

# app_name = 'search'

router = DefaultRouter()
router.register(r'search', SearchView, basename='search')


# url_name_user = [
#     'search-create',
#     'search-update',
#     'search-destroy',
#     'search-soft_delete',
#     'search-create_bulk',
#     'search-update_bulk',
# ]

# url_name_guest = [
#     'search-get'
# ]

# url_user = [
#     *[route for route in router.urls if route.name in url_name_user or route.name=='api-root'],
# ]


# url_guest = [
#     *[route for route in router.urls if route.name in url_name_guest or route.name=='api-root'],
# ]

# urlpatterns = [
#     path('tess/', include(router.urls))
# ]


# urlpatterns+= url_user+ url_guest

# print('r', dir(router), router.urls[0].name, "\n", dir(SearchView))

## GAK JADI karena terlalu ribet untuk mapping karena banyak magic di dalamnya untuk microservice (harus banyak custom), mending define satu" kaya laravel

url_user = [
    path('search/', include([
        path('create', SearchView.as_view({'post': 'create'}), name='search|search.create'),
        path('create_bulk', SearchView.as_view({'post': 'create_bulk'}), name='search|search.create_bulk'),
        path('update/<str:pk>', SearchView.as_view({'put': 'update'}), name='search|search.update'),
        path('update_bulk', SearchView.as_view({'put': 'update_bulk'}), name='search|search.update_bulk'),
        path('destroy/<str:pk>', SearchView.as_view({'delete': 'destroy'}), name='search|search.destroy'),
        path('soft_delete/<str:pk>', SearchView.as_view({'delete': 'soft_delete'}), name='search|search.soft_delete'),
        path('<str:pk>', SearchView.as_view({'get': 'retrieve'}), name='search|search.retrieve'),
    ])),
]

url_guest = [
    path('search/', include([
        path('', SearchView.as_view({'post': 'get'}, permission_classes=[AllowAny]), name='search|search.get')
    ])),
]

urlpatterns = url_user+ url_guest



