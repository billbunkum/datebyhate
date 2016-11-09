from django.conf.urls import include, url
from rest_framework import routers

from interest.viewsets import InterestViewSet, FilmViewSet, UserViewSet, CurrentUserDetails, CreateInterestViewSet, GetHateBuddiesAngst, UserProfileViewSet, UpdateUserProfileViewSet


router = routers.DefaultRouter()
router.register(r'interests', InterestViewSet) #not showing up in API??
router.register(r'films', FilmViewSet)
router.register(r'users', UserViewSet)
router.register(r'create-interests', CreateInterestViewSet)
router.register(r'hate-buddies-angst', GetHateBuddiesAngst)
router.register(r'create-social-links', UserProfileViewSet)
router.register(r'update-social-links', UpdateUserProfileViewSet)

urlpatterns = [
    url(r'^me/$', CurrentUserDetails.as_view(), name="me"),
    url(r'^', include(router.urls)),
]