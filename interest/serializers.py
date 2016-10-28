from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Interest, Film

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'last_login', 'date_joined', 'id', )
        read_only = ('last_login', 'date_joined', 'id', )

class FilmSerializer(serializers.ModelSerializer):
#REDUNDANT
    #custom method field
    # current_user = serializers.SerializerMethodField('_user')

    # #using custom field '_user' to create a method
    # def _user(self, obj):
    #     user = self.context['request'].user
    #     return user

    class Meta:
#   must whitelist 'id' in fields so 'interests' can be persisted by film id
        model = Film
        fields = ('id', 'title', 'genre', 'director', )
#        read_only = ('current_user', )

class InterestSerializer(serializers.ModelSerializer):
    #custom method field; serializerMethodFields are read_only and get their values by calling a method, in this case,  '_user'
    #'()' defaults to get_<field_name>, i.e. get_current_user, which is the def below
    current_user = serializers.SerializerMethodField()
    current_user_id = serializers.SerializerMethodField()

    #using custom field '_user' to create a method
    def get_current_user(self, obj):
        user = self.context['request'].user
        return user

    def get_current_user_id(self, obj):
#        user_id = self.context['request'].user_id
#        user = self.context['request'].user
        return User.objects.get(pk=obj.id)

    #adding 'current_user' w/ request.user as 'user' to fields
    class Meta:
        model = Interest
        fields = ( 'id', 'date', 'current_user', 'current_user_id', 'film', )
        read_only = ( 'id', 'current_user_id', )
