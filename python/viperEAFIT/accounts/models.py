from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from schedules.models import Schedule
from venues.models import Venue
# from academics.models import Program, SubProgram, Course

# from programs.models import Program

# Create your models here.
class User(AbstractUser):
    TEACHER = 'TC'
    COORDINATOR = 'CO'
    ADMIN = 'AD'
    USER_TYPE_CHOICES = (
        (TEACHER, 'Teacher'),
        (COORDINATOR, 'Coordinator'),
        (ADMIN, 'Admin'),
    )
    first_name = models.CharField(max_length=20, blank=False, verbose_name='First Name')
    last_name = models.CharField(max_length=20, blank=False, verbose_name='Last Name')
    email = models.EmailField(blank=False)
    user_type = models.CharField(max_length=15, choices=USER_TYPE_CHOICES, blank=False, verbose_name='User Type')


class Coordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Teacher(models.Model):
    NOVICIO = 'NV'
    DOCENTE = 'DC'
    MASTER = 'MA'
    STATUS_CHOICES = (
        (NOVICIO, 'Novicio'),
        (DOCENTE, 'Docente'),
        (MASTER, 'Master'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identification = models.BigIntegerField(unique=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=NOVICIO, blank=True)
    maxium_hours = models.IntegerField(
        verbose_name='Maxium Hours',
        validators=[MinValueValidator(18), MaxValueValidator(40)],
        blank=True
    )
    availability = models.OneToOneField(Schedule, on_delete=models.CASCADE, blank=True, null=True)
    venues = models.ManyToManyField(Venue, related_name='venues', blank=True)

    # Red Flags
    sufficiency = models.BooleanField(default=False)
    simevi = models.BooleanField(verbose_name='SIMEVI', default=False)

    # Gold Stars
    coor_eval = models.FloatField(
        verbose_name='Evaluación Cordinador',
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )
    student_eval = models.FloatField(
        verbose_name='Evaluación Estudiante',
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )
    auto_eval = models.FloatField(
        verbose_name='Evaluación Profesor',
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )
    observations = models.FloatField(
        verbose_name='Observaciones',
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )
    pcp = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    