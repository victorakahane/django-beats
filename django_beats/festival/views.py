from django.shortcuts import render
from .models import FestivalDay
import datetime

# Create your views here.
def index(request):
    """
    View function for the index page of the festival app.
    """
    festival_days = FestivalDay.objects.prefetch_related(
        'artists'
    ).order_by('date')

    context = {
        'festival_days': festival_days
    }
    return render(request, 'festival/index.html', context)

    