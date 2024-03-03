from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import FilmForm, FilmDetailForm, CreateFilmForm
from .models import Moovie, Producer, Actor
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
# import requests
# from rest_framework.views import APIView
# from rest_framework import generics, status
# from rest_framework.response import Response
#
'''
 MoovieCreate has taken source data for databases from  https://www.omdbapi.com/ by http request, 
 Firstly i wanted realize this through Rest API and serializators, but it was esely way to do this just through library 
 "requests"
'''
# class MoovieCreate(CreateView):
#     model = Moovie
#
#     def get(self, request):
#         films_data = [
#             'Batman', 'inception', 'titanic', 'terminator', 'bladerunner', 'Interstellar', 'Logan', 'Fightclub',
#             'Gentlemen', 'Waschen, schneiden, legen', 'Kingsman', 'Fury', 'Dont Look Up', 'The Godfather', 'Lara Croft',
#             'Goodfellas', 'The Avengers', 'Iron Man', 'Sherlock Holmes', 'Seven', 'Mad Max', 'Inglourious Basterds',
#             'Spiderman', 'Avatar', 'Drive', 'Gladiator', 'Shreck', 'The Wolf of Wall Street', 'The Social Network',
#             'Titanic'
#         ]
#         for film in films_data:
#             try:
#                 response = requests.get(f'https://www.omdbapi.com/?apikey=8f357ea6&t={film}').json()
#             except:
#                 continue
#             print(response['Title'])
#             moovie_name = response['Title']
#             moovie_year = response['Year']
#             moovie_director = response['Director']
#             moovie_actors = (response['Actors'].split(', '))
#
#             if Producer.objects.filter(name=moovie_director).exists():
#                 moovie_director = Producer.objects.get(name=moovie_director)
#             else:
#                 Producer(name=moovie_director).save()
#                 moovie_director = Producer.objects.get(name=moovie_director)
#
#
#             for actor in moovie_actors:
#                 if Actor.objects.filter(name=actor).exists():
#                     pass
#                 else:
#                     Actor(name=actor).save()
#
#             if Moovie.objects.filter(name=moovie_name).exists():
#                 pass
#             else:
#                 Moovie(name=moovie_name, release_year=moovie_year, producer=moovie_director).save()
#
#             moovie = Moovie.objects.get(name=moovie_name)
#             actors = Actor.objects.filter(name__in=moovie_actors)
#             moovie.actors.add(*actors)

''' Main page with film list. I used "get_queryset" coz i need to paginate list also to filter by author/year or actor'''
class FilmList(ListView):
    model = Moovie
    template_name = 'moviepage/film_list.html'
    paginate_by = 25
    form = FilmForm

    def get_queryset(self):
        qs = super().get_queryset()
        print(self.request.GET)
        form = FilmForm(self.request.GET)
        form.is_valid()
        film_name = form.cleaned_data["name"]
        film_category = form.cleaned_data["category"]
        if film_category == 'producer':
            qs = qs.filter(producer__name__contains=film_name)
        if film_category == 'year':
            qs = qs.filter(release_year__contains=film_name)
        if film_category == 'actor':
            qs = qs.filter(actors__name__contains=film_name).distinct()
        return qs

    def get_context_data(self):
        context = super().get_context_data()
        form = FilmForm(self.request.GET)
        form.is_valid()
        context['form'] = form
        return context

''' "get_context_data" get ititialize data for form and send a POST request to edit a film (were some dificulties with 
actors ManyToMany fild but i handle it)'''
class FilmDetail(DetailView):
    model = Moovie
    template_name = 'moviepage/film_edit.html'
    form = FilmDetailForm

    def get_context_data(self, **kwargs):
        pk = kwargs['object'].pk
        data = kwargs['object']
        actors = ''
        for actor in data.actors.all():
            actors += str(actor.name) + ', '

        initial_dict = {
            'name' : data.name,
            'producer' : data.producer.name,
            'year' : data.release_year,
            'actors' : actors,
        }
        form = FilmDetailForm(initial=initial_dict)
        context = super().get_context_data(**kwargs)
        context['form'] = form
        context['pk'] = pk
        return context

    def post(self, *args, **kwargs):
        form = FilmDetailForm(self.request.POST)
        form.is_valid()
        pk = kwargs['pk']
        producer = None
        movie = Moovie.objects.get(pk=pk)

        actors = self.request.POST['actors'].split(', ')
        if Producer.objects.filter(name=form.cleaned_data['producer']).exists():
            producer = Producer.objects.get(name=form.cleaned_data['producer'])
        else:
            Producer(name=form.cleaned_data['producer']).save()
            producer = Producer.objects.get(name=form.cleaned_data['producer'])

        if movie.name != form.cleaned_data['name']:
            movie.name = form.cleaned_data['name']
            movie.save()
        if movie.release_year != form.cleaned_data['year']:
            movie.release_year = form.cleaned_data['year']
            movie.save()
        if movie.producer != form.cleaned_data['producer']:
            movie.producer = producer
            movie.save()


        for actor_name in actors:
            actor = None
            if actor_name == ', ':
                continue
            if Actor.objects.filter(name=actor_name).exists():
                actor = Actor.objects.get(name=actor_name)
            else:
                Actor(name=actor_name).save()
                actor = Actor.objects.get(name=actor_name)

            if actor in movie.actors.all():
                pass
            else:
                movie.actors.add(actor)
        return redirect('film-list')

''' Class to Delete moovie'''
class FilmDelete(DeleteView):
    model = Moovie

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        movie_to_delete = Moovie.objects.get(pk=pk)
        movie_to_delete.delete()
        return redirect('film-list')


''' Class to Create moovie'''
class FilmCreate(CreateView):
    model = Moovie
    template_name = 'moviepage/film_create.html'
    form_class = CreateFilmForm
    success_url = reverse_lazy('film-list')

