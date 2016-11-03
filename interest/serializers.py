from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Interest, Film

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'last_login', 'date_joined', 'id', )
        read_only_fields = ('last_login', 'date_joined', 'id', )

class FilmSerializer(serializers.ModelSerializer):

    class Meta:
#   must whitelist 'id' in fields so 'interests' can be persisted by film id
        model = Film
        fields = ('id', 'title', 'genre', 'director', 'imdbID', 'plot', )
#        read_only = ('current_user', )

class InterestSerializer(serializers.ModelSerializer):
    film = FilmSerializer()
    class Meta:
        model = Interest
        fields = ( 'id', 'date', 'user', 'film', 'imdbID', )
        read_only_fields = ( 'id', 'user', 'film', 'imdbID', )

class CreateInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ( 'id', 'date', 'user', 'film', 'imdbID', )