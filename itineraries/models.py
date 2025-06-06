from django.db import models
from django.conf import settings  


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
