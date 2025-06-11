from rest_framework import serializers
from .models import Itinerary

class ItinerarySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Itinerary
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username
        }
