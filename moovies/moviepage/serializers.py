from rest_framework import serializers
from .models import Moovie

class MoovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moovie
        fields = ('name', 'release_year', 'producer', 'actor',)
