from rest_framework.serializers import ModelSerializer
from .models import Provider


class ProviderSerializer(ModelSerializer):

    class Meta:
        model = Provider
        fields = ('name', 'email', 'phone_number', 'language', 'currency')
