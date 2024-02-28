from django.contrib import admin
from django.urls import path
from .views import MoovieList
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MoovieList.as_view())
]