from rest_framework.serializers import ModelSerializer

from core.models import Imoveis


class ImoveisSerializer(ModelSerializer):
    class Meta:
        model = Imoveis
        fields = "__all__"
