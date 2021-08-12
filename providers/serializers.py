from rest_framework.serializers import ModelSerializer
from .models import Provider


class ProviderSerializer(ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'
