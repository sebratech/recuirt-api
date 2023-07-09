import uuid
from django.conf import settings
from django.db import models

# Create your models here.
class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)

class Position(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skill, through="ExperienceWeight")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class ExperienceWeight(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    time_of_experience = models.DecimalField(decimal_places=1),
    weight = models.IntegerField()
    required = models.BooleanField()
    

