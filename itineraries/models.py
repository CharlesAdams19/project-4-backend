from django.db import models
from django.conf import settings  
from django.db import models


# Create your models here.
class Itinerary(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='itineraries'
    )
    itinerary_items = models.JSONField(default=list)  

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Show(models.Model):
    name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    time = models.CharField(max_length=50)  # "19:30", etc
    dates = models.JSONField(default=list)  # ["2025-08-01", "2025-08-02", ...]

    def __str__(self):
        return f"{self.name} at {self.venue}"
