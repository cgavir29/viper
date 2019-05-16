from django.db import models
from django.utils import timezone
from schedules.models import Schedule
from venues.models import Venue
from accounts.models import Coordinator, Teacher


# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=50, unique=True)
    coordinator = models.OneToOneField(Coordinator, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name


class SubProgram(models.Model):
    name = models.CharField(max_length=30, unique=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher, blank=True)

    class Meta:
        unique_together = ('name', 'program')
        verbose_name = 'Sub-Program'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    subprogram = models.ForeignKey(SubProgram, on_delete=models.CASCADE, verbose_name='Sub-Program')
    teachers = models.ManyToManyField(Teacher, related_name='teachers', blank=True)
    is_active = models.BooleanField(default=True)


    # So there can't be 2 courses with the same name assigned to the same subprogram
    class Meta:
        unique_together = ('name', 'subprogram')

    def __str__(self):
        return self.name

    # def __str__(self):
    #     return f'{self.subprogram} : {self.name}'


class Class(models.Model):
    class Meta:
        verbose_name_plural = 'classes'

    INTENSIVO = 'Intensivo'
    SEMI_INTENSIVO = 'Semi-Intensivo'
    REGULAR = 'Regular'
    INTENSITY_CHOICES = (
        (INTENSIVO, INTENSIVO),
        (SEMI_INTENSIVO, SEMI_INTENSIVO),
        (REGULAR, REGULAR),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    intensity = models.CharField(max_length=15, choices=INTENSITY_CHOICES)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='venue')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='schedule')
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='teacher',
        blank=True,
        null=True
    )
    end_date = models.DateField(verbose_name='End Date (YYYY-MM-DD)', default=timezone.now)
