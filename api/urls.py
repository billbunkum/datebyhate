from django.conf.urls import include, url
from rest_framework import routers

from interest.viewsets import InterestViewSet, FilmViewSet, UserViewSet, CurrentUserDetails, CreateInterestViewSet, GetHateBuddiesAngst


router = routers.DefaultRouter()
router.register(r'interests', InterestViewSet) #not showing up in API??
router.register(r'films', FilmViewSet)
router.register(r'users', UserViewSet)
router.register(r'createInterests', CreateInterestViewSet)
router.register(r'hateBuddiesAngst', GetHateBuddiesAngst)

urlpatterns = [
    url(r'^me/$', CurrentUserDetails.as_view(), name="me"),
    url(r'^', include(router.urls)),
]