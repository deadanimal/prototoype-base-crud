
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
    Assessment, 
)

from .serializers import (
    AssessmentSerializer, 
)


class AssessmentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]    

    
    def get_queryset(self):
        queryset = Assessment.objects.all()
        return queryset    
          
