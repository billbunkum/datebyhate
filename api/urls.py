from django.conf.urls import include, url
from rest_framework import routers

from interest.viewsets import InterestViewSet, FilmViewSet, UserViewSet, CurrentUserDetails, CreateInterestViewSet


router = routers.DefaultRouter()
router.register(r'interests', InterestViewSet)
router.register(r'films', FilmViewSet)
router.register(r'users', UserViewSet)
router.register(r'createInterests', CreateInterestViewSet)

urlpatterns = [
    url(r'^me/$', CurrentUserDetails.as_view(), name="me"),
    url(r'^', include(router.urls)),
]