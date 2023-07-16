from django.contrib import admin
from .models import Position, Skill, ExperienceWeight, Vacancy

class ExperienceWeightInline(admin.TabularInline):
    model = ExperienceWeight
    extra = 1
    autocomplete_fields = ['skill']

class SkillAdmin(admin.ModelAdmin):
    inlines = (ExperienceWeightInline,)
    search_fields = ('name',)

class PositionAdmin(admin.ModelAdmin):
    inlines = (ExperienceWeightInline,)

# Register your models here.
admin.site.register(Position, PositionAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Vacancy)
