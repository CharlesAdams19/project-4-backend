from django.urls import path
from .views import ItineraryListCreateView, ItineraryDetailView, AllItinerariesListView
from django.urls import path
from .views import ShowListView

urlpatterns = [
    path('', ItineraryListCreateView.as_view()),
    path('all/', AllItinerariesListView.as_view()),             
    path('<int:pk>/', ItineraryDetailView.as_view()),
    path('shows/', ShowListView.as_view(), name='show-list'),
]

