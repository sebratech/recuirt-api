from django.urls import path, include
from rest_framework import routers

from .views import SkillsViewSet, ExperiencesViewSet, PositionsViewSet, VacanciesViewSet

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

router = routers.DefaultRouter()
router.register(r"skills", SkillsViewSet)
router.register(r"positions", PositionsViewSet)
router.register(r"experiences", ExperiencesViewSet)
router.register(r"vacancies", VacanciesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
