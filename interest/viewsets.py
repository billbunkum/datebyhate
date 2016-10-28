from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView

from django.contrib.auth.models import User

from .models import Interest, Film
from .serializers import InterestSerializer, UserSerializer, FilmSerializer

class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
#   notifies router.urls in api to go through InterestSerializer (whitelist, blacklist) models

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class CurrentUserDetails(RetrieveAPIView):
    model = User
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user