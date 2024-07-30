from django.urls import path
from .views import HouseListView, HouseDetailView, EntranceDetailView

urlpatterns = [
    path('', HouseListView.as_view(), name='house_list'),
    path('<int:pk>/', HouseDetailView.as_view(), name='house_detail'),
    path('entrance/<int:pk>/', EntranceDetailView.as_view(), name='entrance_detail'),
]
