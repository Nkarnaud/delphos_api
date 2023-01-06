from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from delphos_api.core.service.loan_service import LoanService
from delphos_api.serializers import (
    LoanSerializer,
    CountrySerializer,
    SectorSerializer,
    ProjectSerializer
)


class LoanViewSet(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = LoanService().get_loan()
    serializer_class = LoanSerializer

    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)


class CountryViewSet(ListAPIView):
    queryset = LoanService().get_country()
    serializer_class = CountrySerializer


class SectorViewSet(ListAPIView):
    queryset = LoanService().get_sectors()
    serializer_class = SectorSerializer


class ProjectViewSet(ListAPIView):
    queryset = LoanService().get_project()
    serializer_class = ProjectSerializer
