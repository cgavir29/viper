from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from schedules.models import Schedule
from venues.models import Venue


class User(AbstractUser):
    ADMIN = 'AD'
    COORDINATOR = 'CO'
    TEACHER = 'TC'
    USER_TYPE_CHOICES = (
        (ADMIN, 'Admin'),
        (COORDINATOR, 'Coordinator'),
        (TEACHER, 'Teacher'),
    )

    first_name = models.CharField(max_length=20, blank=False, verbose_name='First Name')
    last_name = models.CharField(max_length=20, blank=False, verbose_name='Last Name')
    email = models.EmailField(blank=False)
    epik_unique_number = models.BigIntegerField(
        unique=True,
        verbose_name='Epik Unique Number',
        validators=[MinValueValidator(0), MaxValueValidator(9999999999)],
        blank=True,
        null=True
    ) # Cambiar el blank, y null
    user_type = models.CharField(
        max_length=15,
        choices=USER_TYPE_CHOICES,
        verbose_name='User Type'
    )


class Teacher(models.Model):
    NOVICIO = 'Novicio'
    DOCENTE = 'Docente'
    MASTER = 'Master'
    STATUS_CHOICES = (
        (NOVICIO, NOVICIO),
        (DOCENTE, DOCENTE),
        (MASTER, MASTER),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=NOVICIO, blank=True)
    available_hours = models.IntegerField(
        verbose_name='Available Hours',
        validators=[MinValueValidator(0), MaxValueValidator(40)],
        default=0
    )
    availability = models.OneToOneField(Schedule, on_delete=models.CASCADE, blank=True, null=True)
    venues = models.ManyToManyField(Venue, related_name='venues', blank=True)
    sufficiency = models.BooleanField(default=False)
    simevi = models.BooleanField(verbose_name='SIMEVI', default=False)
    pdp = models.BooleanField(verbose_name='PDP', default=False)
    coor_eval = models.FloatField(
        verbose_name='Coordinator Evaluation',
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )
    student_eval = models.FloatField(
        verbose_name='Student Evaluation',
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )
    self_eval = models.FloatField(
        verbose_name='Self-Evaluation',
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )
    observations = models.FloatField(
        verbose_name='Observations',
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )
    


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
