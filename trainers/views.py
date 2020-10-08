
from django.shortcuts import render
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin


from django_filters.rest_framework import DjangoFilterBackend


from .models import (
    Trainer, 
)

from .serializers import (
    TrainerSerializer, 
)


class TrainerViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        user = self.request.user
      
        return queryset  
          

    @action(methods=['GET'], detail=True)
    def activate(self, request, *args, **kwargs):
        Trainer = self.get_object()
        Trainer.active = True

        serializer =  TrainerSerializer(Trainer)
        return Response(serializer.data)   

    @action(methods=['GET'], detail=True)
    def deactivate(self, request, *args, **kwargs):
        Trainer = self.get_object()
        Trainer.active = False

        serializer =  TrainerSerializer(Trainer)
        return Response(serializer.data)        
