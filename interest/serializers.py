from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Interest, Film

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'last_login', 'date_joined', 'id', )
        read_only = ('last_login', 'date_joined', 'id', )

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
#   must whitelist 'id' in fields so 'interests' can be persisted by film id
        model = Film
        fields = ('id', 'title', 'genre', 'director', )

class InterestSerializer(serializers.ModelSerializer):
    #custom method field
    current_user = serializers.SerializerMethodField('_user')

    #using custom field '_user' to create a method
    def _user(self, obj):
        user = self.context['request'].user
        return user

    #adding 'current_user' w/ request.user as 'user' to fields
    class Meta:
        model = Interest
        fields = ( 'id', 'date', 'current_user', 'film', )
        read_only = ( 'id', 'current_user', )
