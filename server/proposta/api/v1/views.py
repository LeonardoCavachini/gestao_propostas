from .serializers import PropostasSerializer
from rest_framework import viewsets
from proposta.models import Proposta


class PropostasViewSet(viewsets.ModelViewSet):
    queryset = Proposta.objects.all()
    serializer_class = PropostasSerializer
