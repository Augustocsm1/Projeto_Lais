from rest_framework import serializers
from atendimento import models

class atendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.atendimento
        fields = "__all__"