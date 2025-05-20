from django.contrib import admin
from .models import FestivalDay, Artist

class ArtistInline(admin.TabularInline):
    """
    Inline admin interface for the Artist model.
    """
    model = Artist
    extra = 1 # Number of empty forms to display

@admin.register(FestivalDay)
class FestivalDayAdmin(admin.ModelAdmin):
    """
    Admin interface for the FestivalDay model.
    """
    inlines = [ArtistInline] # Show artists inline in the FestivalDay admin
    list_display = ('date',)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """
    Admin interface for the Artist model.
    """
    list_display = ('name', 'performance_time', 'genre', 'day') # Show name, performance time, genre, and day in the admin
    list_filter = ('day', 'genre') # Side filter for days and genres
    ordering = ('day', 'performance_time')
