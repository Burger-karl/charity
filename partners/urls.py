from django.urls import path
from . import views

urlpatterns = [
    path('partner/', views.partner_form_view, name='partner_form'),
    path('volunteer/', views.volunteer_form_view, name='volunteer_form'),
]
