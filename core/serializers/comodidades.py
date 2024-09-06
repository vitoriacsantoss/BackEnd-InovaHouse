from rest_framework.serializers import ModelSerializer

from core.models import Comodidade


class ComodidadeSerializer(ModelSerializer):
    class Meta:
        model = Comodidade
        fields = "__all__"
