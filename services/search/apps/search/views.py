from django.shortcuts import render
from rest_framework import viewsets, mixins, generics, views
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, parser_classes, action
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from search.functions.crud.crud import CRUD1
from search.forms import forms
from django import forms as f_dj
from main.response_helper import message_error, response_builder

class SearchView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly] # this will be default, double check overriding in urls
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get(self, request):
        data = request.data
        print('ini2', data)

        form = None
        try:

            form = forms.SearchGetForm(data=data)
            if form.is_valid() is False:
                print('11111122222222', form.cleaned_data)
                raise f_dj.ValidationError('validation error')
            cls = CRUD1(form.cleaned_data.get('collection'))
            data = cls.get(form.cleaned_data['data'], form.cleaned_data['soft_delete'])

        except f_dj.ValidationError as e:
            return response_builder({'error': form.errors}, 400)
        except Exception as e:
            return response_builder({'error': message_error(e)}, 500)


        return response_builder(data, 200)

    def create(self, request):
        data = request.data

        form = None
        try:
            form = forms.SearchAddParam(data)
            if form.is_valid() is False:
                raise f_dj.ValidationError('validataion error')

            cls = CRUD1(form.cleaned_data['collection'])
            data = cls.add(form.cleaned_data['data'])
        except f_dj.ValidationError as e:
            return response_builder({'error': form.errors}, 400)
        except Exception as e:
            return response_builder({'error': message_error(e)}, 500)

        return response_builder(data, 200)

    def update(self, request, pk=None):
        data = request.data

        form = None
        try:
            data['id']= pk

            form = forms.SearchUpdateParam(data)
            if form.is_valid() is False:
                raise f_dj.ValidationError('validataion error')

            cls = CRUD1(form.cleaned_data['collection'])
            data = cls.update(form.cleaned_data['id'], form.cleaned_data['data'])
        except f_dj.ValidationError as e:
            return response_builder({'error': form.errors}, 400)
        except Exception as e:
            return response_builder({'error': message_error(e)}, 500)

        return response_builder(data, 200)


    def destroy(self, request, pk=None):
        data = request.data.copy()
        form = None

        try:
            data['id']= pk

            form = forms.SearchDeleteParam(data)
            if form.is_valid() is False:
                raise f_dj.ValidationError('validataion error')

            cls = CRUD1(form.cleaned_data['collection'])
            data = cls.delete(form.cleaned_data['id'])
        except f_dj.ValidationError as e:
            return response_builder({'error': form.errors}, 400)
        except Exception as e:
            return response_builder({'error': message_error(e)}, 500)

        return response_builder(data, 200)

    def retrieve(self, request, pk=None):
        return Response({})

    # this wrapper will use in generate .as_view() when called
    # this wrapper will be run if you not override as_view params in route level. must end with Class.as_view without ()
    @action(
        methods=['delete'],
        detail=True, # for action that need pk param
        url_name='soft_delete',
        permission_classes=[IsAuthenticated] # to override default permission_classes, other param level class is avaible
    )
    def soft_delete(self, request, pk=None):
        data= request.data.copy()
        form = None

        try:
            data['id']= pk

            form = forms.SearchDeleteParam(data)
            if form.is_valid() is False:
                raise f_dj.ValidationError('validataion error')

            cls = CRUD1(form.cleaned_data['collection'])
            data = cls.soft_delete(form.cleaned_data['id'])
        except f_dj.ValidationError as e:
            return response_builder({'error': form.errors}, 400)
        except Exception as e:
            return response_builder({'error': message_error(e)}, 500)

        return response_builder(data, 200)

    @action(methods=['post'], detail=False, url_name='create_bulk')
    def create_bulk(self, request):
        return Response({})

    @action(methods=['put'], detail=False, url_name='update_bulk')
    def update_bulk(self, request):
        return Response({})



