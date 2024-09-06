from rest_framework.viewsets import ModelViewSet

from core.models import Comodidade
from core.serializers import ComodidadeSerializer


class ComodidadeViewSet(ModelViewSet):
    queryset = Comodidade.objects.all().order_by("id")
    serializer_class = ComodidadeSerializer
