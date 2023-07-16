from rest_framework import serializers
from .models import Skill, Position, ExperienceWeight, Vacancy

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('__all__')

class ExperiencesWeightSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source="skill.name")
    id = serializers.ReadOnlyField(source="skill.id")
    class Meta:
        model = ExperienceWeight
        fields = ('id', 'name', 'experience_time' ,'weight', 'name', 'required')

class PositionsSerializer(serializers.ModelSerializer):
    skills = ExperiencesWeightSerializer(many=True, source="experienceweight_set")
    class Meta:
        model = Position
        fields = ('id', 'name', 'description', 'skills')
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        print(validated_data)
        experience_weights = validated_data.pop('experienceweight_set')
        position = Position.objects.create(**validated_data)
        for experience_weight in experience_weights:
            skill_name = experience_weight.pop('name')
            skill = Skill.object.get_or_create(name=skill_name)
            ExperienceWeight.objects.create(position=position, skill=skill, **skill_experience)
        return position

class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('__all__')
