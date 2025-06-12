from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Itinerary
from .serializers import ItinerarySerializer
from rest_framework.generics import ListAPIView
from .models import Show
from .serializers import ShowSerializer
from rest_framework.exceptions import PermissionDenied



class ItineraryListCreateView(ListCreateAPIView):
    # queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Itinerary.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ItineraryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
    permission_classes = [IsAuthenticated]

class AllItinerariesListView(ListAPIView):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
    permission_classes = [IsAuthenticated]

class ShowListView(ListAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class ItineraryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        itinerary = super().get_object()
        if self.request.method in ['PATCH', 'DELETE']:
            if itinerary.user != self.request.user:
                raise PermissionDenied("You do not have permission to edit this itinerary.")
        return itinerary