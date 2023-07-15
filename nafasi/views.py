from django.shortcuts import render
from rest_framework import viewsets, permissions

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

