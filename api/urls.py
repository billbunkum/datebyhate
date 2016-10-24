from django.conf.urls import include, url
from rest_framework import routers

from interest.viewsets import InterestViewSet, FilmViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'interests', InterestViewSet)
router.register(r'films', FilmViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
