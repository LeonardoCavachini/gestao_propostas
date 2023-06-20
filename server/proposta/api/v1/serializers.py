from rest_framework import serializers
from proposta.models import Proposta

class PropostasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposta
        fields = '__all__'