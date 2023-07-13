from django.contrib import admin
from .models import Position, Skill, ExperienceWeight, Vacancy

# Register your models here.
admin.site.register(Position)
admin.site.register(ExperienceWeight)
admin.site.register(Skill)
admin.site.register(Vacancy)
