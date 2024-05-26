from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response

class Test(views.APIView):

    def get(self, request):
        print('yaya')
        data = {
            'body': request.body,
            'data': request.data,
            'meta': dir(request),
            'header': request.headers,
            'get': request.query_params,
            'post': request.POST,
            'url': [request.get_full_path_info(), request.get_full_path()],
        }

        return Response(data=data, status=200)
