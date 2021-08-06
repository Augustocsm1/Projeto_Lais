from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from locais.api import serializers
from locais import models

class locaisViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    serializer_class = serializers.locaisSerializer
    queryset = models.locais.objects.all()