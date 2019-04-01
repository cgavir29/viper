from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class SubProgram(models.Model):
    name = models.CharField(max_length=30, unique=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'program')
        
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    subprogram = models.ForeignKey(SubProgram, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    # So there can't be 2 courses with the same name assigned to the same subprogram
    class Meta:
        unique_together = ('name', 'subprogram')

    def __str__(self):
        return f'{self.subprogram} : {self.name}'
