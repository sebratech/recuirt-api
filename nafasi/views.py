from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.db import transaction

from .models import Skill, Position, ExperienceWeight, Vacancy
from .serializers import SkillsSerializer, PositionsSerializer, ExperiencesWeightSerializer, VacanciesSerializer

# Create your views here.

class SkillsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [permissions.IsAuthenticated]

class PositionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Position.objects.all()
    serializer_class = PositionsSerializer
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def create(self, request):
        position_data = request.data
        position_data['author'] = request.user.id
        serializer = self.serializer_class(data=position_data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExperiencesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ExperienceWeight.objects.all()
    serializer_class = ExperiencesWeightSerializer
    permission_classes = [permissions.IsAuthenticated]

class VacanciesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vacancy.objects.all()
    serializer_class = VacanciesSerializer
    permission_classes = [permissions.IsAuthenticated]
