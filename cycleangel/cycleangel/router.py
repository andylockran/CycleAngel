from rest_framework import routers

from incident.models import IncidentViewSet

router = routers.DefaultRouter()
router.register(r'incident', IncidentViewSet)
