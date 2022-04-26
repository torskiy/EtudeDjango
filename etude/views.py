from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import *


# Create your views here.


class HomeView(TemplateView):
    """Главная страница"""

    template_name = 'etude/home_test.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class ContactUsView(TemplateView):
    """Страница Связаться"""

    template_name = 'etude/contact_us.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Связаться'
        return context


class CasesView(ListView):
    """Портфолио"""

    model = Case
    template_name = 'etude/works.html'
    context_object_name = 'cases'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Работы'
        return context

    def get_queryset(self):
        return Case.objects.filter(is_published=True)


class ViewCase(DetailView):
    """Отображение конкретного кейса"""

    model = Case
    context_object_name = 'case'
    template_name = 'etude/view_case.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Работы'
        return context


class AboutUsView(ListView):
    """Страница О нас"""

    model = Contact
    template_name = 'etude/about_us.html'
    context_object_name = 'contacts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас'
        return context

    def get_queryset(self):
        return Contact.objects.filter(is_published=True)

