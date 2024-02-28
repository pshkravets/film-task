from django.shortcuts import render
from django.views.generic import ListView
# import requests

class MoovieList(ListView):
    template_name = 'mooviepage/film_list.html'
    model = None

    def get(self, *args, **kwargs):
        return super(MoovieList, self).get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        print('Hello World!!!')
        print(kwargs)
        context = {}
        return context