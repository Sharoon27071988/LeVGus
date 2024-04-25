from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from .models import DecorativePlaster, Category


class HomeView(ListView):
    template_name = 'paster/home.html'
    model = DecorativePlaster
    context_object_name = 'paster'
    extra_context = {'home': True}
    paginate_by = 8


class CategoryView(ListView):
    template_name = 'paster/category.html'
    model = DecorativePlaster
    context_object_name = 'paster'
    extra_context = {'catalog': True}
    paginate_by = 8

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return DecorativePlaster.objects.filter(type__category=category)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = get_object_or_404(Category, pk=self.kwargs['pk'])
        return context


class DecorativePlasterDetailView(DetailView):
    template_name = 'paster/paster_detail.html'
    model = DecorativePlaster
    context_object_name = 'paster'


class CompanyInfoView(TemplateView):
    template_name = 'paster/company_info.html'
    extra_context = {'company_info': True}


class CooperatioInfo(TemplateView):
    template_name = 'paster/cooperation_info.html'
    extra_context = {'cooperation_info': True}