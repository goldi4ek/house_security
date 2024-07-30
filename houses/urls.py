from django.urls import path
from .views import HouseListView, HouseDetailView, EntranceDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", HouseListView.as_view(), name="house_list"),
    path("<int:pk>/", HouseDetailView.as_view(), name="house_detail"),
    path("entrance/<int:pk>/", EntranceDetailView.as_view(), name="entrance_detail"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
