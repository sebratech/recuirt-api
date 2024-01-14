from rest_framework import serializers
from .models import Skill, Position, ExperienceWeight, Vacancy


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class ExperiencesWeightSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="skill.name")

    class Meta:
        model = ExperienceWeight
        fields = ("id", "name", "experience_time", "weight", "required")


class PositionsSerializer(serializers.ModelSerializer):
    skills = ExperiencesWeightSerializer(many=True, source="experienceweight_set")

    class Meta:
        model = Position
        fields = ("id", "name", "description", "author", "skills")
        extra_kwargs = {"skills": {"required": True, "read_only": False}}
        read_only_fields = ("created_at",)

    def create(self, validated_data):
        experience_weights = validated_data.pop("experienceweight_set")
        position = Position.objects.create(**validated_data)
        for experience_weight in experience_weights:
            skill_data = experience_weight.pop("skill")
            skill, _ = Skill.objects.get_or_create(name=skill_data["name"].lower())
            ExperienceWeight.objects.create(
                position=position, skill=skill, **experience_weight
            )
        return position

    def update(self, instance, validated_data):
        experience_weights = validated_data.pop("experienceweight_set")
        instance.name = validated_data.pop("name")
        instance.description = validated_data.pop("description")
        instance.save()

        # List of skill IDs to keep
        updated_skill_ids = []

        for experience_weight_data in experience_weights:
            skill_data = experience_weight_data.get("skill", {})
            skill_name = skill_data.get("name").lower()
            weight = experience_weight_data.get("weight", 0)
            required = experience_weight_data.get("required", False)
            experience_time = experience_weight_data.get("experience_time", None)
            skill, _ = Skill.objects.get_or_create(name=skill_name)
            updated_skill_ids.append(skill.id)

            experience_weight, created = ExperienceWeight.objects.get_or_create(
                position=instance,
                skill=skill,
                defaults={
                    "weight": weight,
                    "required": required,
                    "experience_time": experience_time,
                },
            )
            if not created:
                experience_weight.weight = weight
                experience_weight.required = required
                experience_weight.experience_time = experience_time
                experience_weight.save()

        # Delete ExperienceWeight instances not in the updated skills list
        ExperienceWeight.objects.filter(position=instance).exclude(
            skill_id__in=updated_skill_ids
        ).delete()

        return instance


class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")
