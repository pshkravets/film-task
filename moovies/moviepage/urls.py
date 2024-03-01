from django.contrib import admin
from django.urls import path
from .views import FilmList, FilmCreate, FilmDetail, FilmDelete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_film/', FilmList.as_view(), name='film-list'),
    path('film_detail/<int:pk>', FilmDetail.as_view(), name='film-edit'),
    path('film_delete/<int:pk>', FilmDelete.as_view(), name='film-delete'),
    path('film_create/', FilmCreate.as_view(), name='film-create'),
]