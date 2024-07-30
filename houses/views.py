from django.shortcuts import render, get_object_or_404
from .models import House, Entrance, Apartment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

class HouseListView(LoginRequiredMixin, ListView):
    model = House
    template_name = 'houses/house_list.html'
    context_object_name = 'houses'

class HouseDetailView(LoginRequiredMixin, DetailView):
    model = House
    template_name = 'houses/house_detail.html'
    context_object_name = 'house'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entrances'] = Entrance.objects.filter(house=self.object)
        return context

class EntranceDetailView(LoginRequiredMixin, DetailView):
    model = Entrance
    template_name = 'houses/entrance_detail.html'
    context_object_name = 'entrance'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apartments'] = Apartment.objects.filter(entrance=self.object)
        return context
