import uuid
from django.conf import settings
from django.db import models
from user.models import CustomUser

# Create your models here.
class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Position(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skill, through="ExperienceWeight")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(CustomUser.get_fallback_pk))

    def __str__(self) -> str:
        return self.name
    

class ExperienceWeight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    experience_time = models.DecimalField(max_digits=3, decimal_places=1)
    weight = models.IntegerField()
    required = models.BooleanField()

    def __str__(self) -> str:
        return self.skill.name
    

class Vacancy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    max_candidates = models.IntegerField()
    due_date = models.DateField()
    min_threshold = models.IntegerField()
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name="%(app_label)s_%(class)s_responsible", related_query_name="%(app_label)s_%(class)ss")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(CustomUser.get_fallback_pk), default=CustomUser.get_fallback_pk)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.position.name
    

