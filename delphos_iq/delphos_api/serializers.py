import uuid
from rest_framework import serializers

from delphos_api.models import Loans


class LoanSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(default=uuid.uuid4)
    title = serializers.CharField(max_length=255)
    country = serializers.CharField(max_length=50)
    sector = serializers.CharField(max_length=128)
    amount = serializers.CharField(max_length=50)

    class Meta:
        model = Loans
        fields = '__all__'


class CountrySerializer(serializers.Serializer):
    country = serializers.CharField(max_length=50)


class ProjectSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)


class SectorSerializer(serializers.Serializer):
    sector = serializers.CharField(max_length=50)


