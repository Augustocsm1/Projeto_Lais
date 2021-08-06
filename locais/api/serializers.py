from rest_framework import serializers
from locais import models

class locaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.locais
        fields = "__all__"