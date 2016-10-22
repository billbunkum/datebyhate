from django.conf.urls import include, url
from rest_framework import routers

from interest.viewsets import InterestViewSet

router = routers.DefaultRouter()
router.register(r'interests', InterestViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
#   i do this so that 'pointing to' an interest does not change the URL/page; as Angular updates a component on the fly??