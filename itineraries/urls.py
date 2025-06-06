from django.urls import path
from .views import ItineraryListCreateView, ItineraryDetailView, AllItinerariesListView

urlpatterns = [
    path('', ItineraryListCreateView.as_view()),
    path('all/', AllItinerariesListView.as_view()),             
    path('<int:pk>/', ItineraryDetailView.as_view()),
]

