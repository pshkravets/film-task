from django.shortcuts import render
from django.views.generic import ListView
import requests
from .models import Moovie
from rest_framework import generics

class MoovieAPIView(generics.ListAPIView):
    queryset = Moovie.objects.all()

class MoovieList(ListView):
    template_name = 'moviepage/film_list.html'
    model = Moovie

    def get(self, *args, **kwargs):
        return super(MoovieList, self).get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = kwargs

        r = requests.get('https://www.omdbapi.com/?apikey=8f357ea6&t=Batman').json()
        print('here')
        print(r)
        # print(r.title)

        # film = Moovie()
        # film.name =
        return context