from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class SubProgram(models.Model):
    name = models.CharField(max_length=30, unique=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    subprogram = models.ForeignKey(SubProgram, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

