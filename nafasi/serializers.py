from rest_framework import serializers
from .models import Skill, Position, ExperienceWeight, Vacancy

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('__all__')

class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('__all__')

class ExperiencesWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceWeight
        fields = ('__all__')

class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('__all__')