from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('works/', CasesView.as_view(), name='works'),
    path('works/<slug>/', ViewCase.as_view(), name='view_case'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('contact_us/', ContactUsView.as_view(), name='contact_us'),
]
