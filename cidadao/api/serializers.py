from rest_framework import serializers
from cidadao import models

class cidadaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.cidadao
        fields = "__all__"