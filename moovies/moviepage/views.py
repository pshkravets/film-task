from django.shortcuts import render
from django.views.generic import ListView


class MoovieList(ListView):
    template_name = 'mooviepage/film_list.html'
    model = None

    def get_context_data(self, *args, **kwargs):
        print('Hello World!!!')
        print(kwargs)
        context = {}
        return context