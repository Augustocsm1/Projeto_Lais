from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from cidadao.api import serializers
from cidadao import models

class cidadaoViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    serializer_class = serializers.cidadaoSerializer
    queryset = models.cidadao.objects.all()