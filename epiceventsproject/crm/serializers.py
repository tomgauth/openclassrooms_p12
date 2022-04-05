from rest_framework.serializers import ModelSerializer
from .models import Contract


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'sales_contact', 'client', 'status']

