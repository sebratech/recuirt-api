from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from django.db import transaction

from .models import Skill, Position, ExperienceWeight, Vacancy
from .serializers import (
    SkillsSerializer,
    PositionsSerializer,
    ExperiencesWeightSerializer,
    VacanciesSerializer,
)
from .utils import (
    set_serializer_author_and_response,
    set_serializer_author_response_update,
)

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
        return set_serializer_author_and_response(self, request)

    @transaction.atomic
    def update(self, request, pk=None):
        position = get_object_or_404(Position, pk=pk)
        return set_serializer_author_response_update(self, request, position)


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

    def create(self, request):
        return set_serializer_author_and_response(self, request)
