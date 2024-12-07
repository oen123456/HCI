from django.urls import path
from .views import check_credibility

urlpatterns = [
    path('check-credibility/', check_credibility, name='check_credibility'),
]
