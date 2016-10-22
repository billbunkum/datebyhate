from rest_framework import viewsets

from .models import Interest
from .serializers import InterestSerializer

class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
#   not sure why I need serializer_class...
# it seems I could simply import InterestSerializer elsewhere?