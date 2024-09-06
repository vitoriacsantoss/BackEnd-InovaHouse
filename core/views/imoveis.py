from rest_framework.viewsets import ModelViewSet

from core.models import Imoveis
from core.serializers import ImoveisSerializer

class ImoveisViewSet(ModelViewSet):
    queryset = Imoveis.objects.all().order_by("id")
    serializer_class = ImoveisSerializer
