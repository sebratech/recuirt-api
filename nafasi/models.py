from django.db import models

# Create your models here.
class Skill(models.Model):
    name = Models.Charfield(max_length=100)

class Position(models.Model):
    name = Models.Charfield(max_length=200)
    description = Models.Textfield()
    created_at=models.DateTimeField(auto_now_add=True)

