from django.db import models
from multiselectfield import MultiSelectField


class Schedule(models.Model):
    TIME_CHOICES = (
        ('6', '6:00 - 7:00'),
        ('7', '7:00 - 8:00'),
        ('8', '8:00 - 9:00'),
        ('9', '9:00 - 10:00'),
        ('10', '10:00 - 11:00'),
        ('11', '11:00 - 12:00'),
        ('12', '12:00 - 13:00'),
        ('13', '13:00 - 14:00'),
        ('14', '14:00 - 15:00'),
        ('15', '15:00 - 16:00'),
        ('16', '16:00 - 17:00'),
        ('17', '17:00 - 18:00'),
        ('18', '18:00 - 19:00'),
        ('19', '19:00 - 20:00'),
        ('20', '20:00 - 21:00')
    )


    INTENSIVO = 'Intensivo'
    SEMI_INTENSIVO = 'Semi-Intensivo'
    REGULAR = 'Regular'
    INTENSITY_CHOICES = (
        (INTENSIVO, INTENSIVO),
        (SEMI_INTENSIVO, SEMI_INTENSIVO),
        (REGULAR, REGULAR),
    )

    name = models.CharField(max_length=100, unique=True)
    intensity = models.CharField(max_length=15, choices=INTENSITY_CHOICES)
    monday = MultiSelectField(choices=TIME_CHOICES, blank=True, null=True)
    tuesday = MultiSelectField(choices=TIME_CHOICES, blank=True, null=True)
    wednesday = MultiSelectField(choices=TIME_CHOICES, blank=True, null=True)
    thursday = MultiSelectField(choices=TIME_CHOICES, blank=True, null=True)
    friday = MultiSelectField(choices=TIME_CHOICES, blank=True, null=True)
    saturday = MultiSelectField(choices=TIME_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name
