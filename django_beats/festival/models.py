from django.db import models

class FestivalDay(models.Model):
    """
    Represents a day in a festival.
    """
    date = models.DateField(unique=True) # Unique date for each festival day
    
    class Meta:
        ordering = ['date'] # Order by date
    
    def __str__(self):
        return self.date.strftime('%B %d, %Y') # Show date in format "February 18, 2025"

class Artist(models.Model):
    """
    Represents an artist performing at the festival.
    """
    name = models.CharField(max_length=100) # Name of the artist
    performance_time = models.TimeField() # Time of performance
    day = models.ForeignKey(FestivalDay, on_delete=models.CASCADE, related_name='artists') # Foreign key to FestivalDay
    
    class Meta:
        ordering = ['performance_time'] # Order by performance time
    
    def __str__(self):
        return f'{self.name} - {self.performance_time.strftime('%H:%M')}' # Show name and time in format "Olivia Rodrigo - 21:00"
