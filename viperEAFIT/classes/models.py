from django.db import models
from accounts.models import Teacher
from academics.models import Course
from schedules.models import Schedule
from venues.models import Venue
from django.utils import timezone

# Create your models here.
class Class(models.Model):
    SEMESTRAL = 'SM'
    REGULAR = 'RE'
    SEMI_INTENSIVO = 'SI'
    INTENSIVO = 'IN'
    ULTRA = 'UL'

    INTENSITY_CHOICES = (
        # (ULTRA, 'Ultra'),
        (INTENSIVO, 'Intensivo'),
        # (SEMESTRAL, 'Semestral'),
        (SEMI_INTENSIVO, 'Semi-Intensivo'),
        (REGULAR, 'Regular'),
        
    )

    # class_code =  models.CharField(max_length=15)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    intensity = models.CharField(max_length=15, choices=INTENSITY_CHOICES)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name='Start Date (YYYY-MM-DD)', default=timezone.now)

    class Meta:
        verbose_name_plural = 'classes' # For plurals



