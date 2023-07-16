from rest_framework import serializers
from .models import Skill, Position, ExperienceWeight, Vacancy

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('__all__')

class ExperiencesWeightSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="skill.name")
    id = serializers.CharField(source="skill.id", required=False)
    class Meta:
        model = ExperienceWeight
        fields = ('id', 'name', 'experience_time' ,'weight', 'required')

class PositionsSerializer(serializers.ModelSerializer):
    skills = ExperiencesWeightSerializer(many=True, source="experienceweight_set")
    class Meta:
        model = Position
        fields = ('id', 'name', 'description', 'author', 'skills')
        extra_kwargs = {
            'skills': { 'required': True, 'read_only': False }    
        }
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        experience_weights = validated_data.pop('experienceweight_set')
        position = Position.objects.create(**validated_data)
        for experience_weight in experience_weights:
            skill_data = experience_weight.pop('skill')
            skill, _ = Skill.objects.get_or_create(name=skill_data['name'].lower())
            ExperienceWeight.objects.create(position=position, skill=skill, **experience_weight)
        return position

class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('__all__')
