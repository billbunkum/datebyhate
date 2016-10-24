from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Interest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', )

class InterestSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Interest
        fields = ( 'date', 'user', 'film', )
        read_only = ( 'date', )

