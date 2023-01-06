from django.urls import path, include
from rest_framework import routers

from delphos_api.views import LoanViewSet, CountryViewSet, SectorViewSet, ProjectViewSet

router = routers.SimpleRouter()
router.register('api/loans', LoanViewSet)


urlpatterns = [
   path('', include(router.urls)),
   path('api/countries', CountryViewSet.as_view(), name='country-list'),
   path('api/sectors', SectorViewSet.as_view(), name='country-list'),
   path('api/projects', ProjectViewSet.as_view(), name='country-list')
]
