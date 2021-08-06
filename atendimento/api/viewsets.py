from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from atendimento.api import serializers
from atendimento import models

class atendimentoViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    serializer_class = serializers.atendimentoSerializer
    queryset = models.atendimento.objects.all()