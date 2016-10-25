from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Interest, Film

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', )

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('title', 'genre', 'director', )

class InterestSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Interest
        fields = ( 'date', 'user_id', 'film_id', )