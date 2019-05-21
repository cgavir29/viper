import os
import django
from escuela import Escuela
from clase import Clase
from horario import Horario
from profesor import Profesor
from lns import gen_rndsol

os.environ['DJANGO_SETTINGS_MODULE'] = 'viperEAFIT.settings'
django.setup()

from schedules.models import Schedule
from academics.models import Class, Course
from accounts.models import Teacher


# -----------------------------------------------------------------
def _cast_range(day_hours):
    result = []
    aux = list(day_hours)

    if aux:
        result = [int(i) for i in aux]

    return result

# -----------------------------------------------------------------
def cast_schedule(class_or_teacher, flag):
    result = Horario()

    if flag == 'c':
        result.set_horario('l', _cast_range(class_or_teacher.schedule.monday), class_or_teacher.id)
        result.set_horario('m', _cast_range(class_or_teacher.schedule.tuesday), class_or_teacher.id)
        result.set_horario('w', _cast_range(class_or_teacher.schedule.wednesday), class_or_teacher.id)
        result.set_horario('j', _cast_range(class_or_teacher.schedule.thursday), class_or_teacher.id)
        result.set_horario('v', _cast_range(class_or_teacher.schedule.friday), class_or_teacher.id)
        result.set_horario('s', _cast_range(class_or_teacher.schedule.saturday), class_or_teacher.id)
    elif flag == 't':
        if class_or_teacher.availability:
            result.set_horario('l', _cast_range(class_or_teacher.availability.monday), '0')
            result.set_horario('m', _cast_range(class_or_teacher.availability.tuesday), '0')
            result.set_horario('w', _cast_range(class_or_teacher.availability.wednesday), '0')
            result.set_horario('j', _cast_range(class_or_teacher.availability.thursday), '0')
            result.set_horario('v', _cast_range(class_or_teacher.availability.friday), '0')
            result.set_horario('s', _cast_range(class_or_teacher.availability.saturday), '0')

    return result

# -----------------------------------------------------------------
def cast_class(cla):
    result = Clase(cla.id, cla.course.id, cla.venue.id)
    result.horario = cast_schedule(cla, 'c')

    return result

# -----------------------------------------------------------------
def cast_teacher(teach):
    prof = Profesor(teach.id, cast_schedule(teach, 't'))
    prof.reqr = set(course.id for course in Course.objects.filter(teachers=teach.id))
    # Red Flags
    prof.variables['sufficiency'] = teach.sufficiency
    prof.variables['simevi'] = teach.simevi
    # Gold Stars
    prof.variables['coor_eval'] = teach.coor_eval
    prof.variables['student_eval'] = teach.student_eval
    prof.variables['auto_eval'] = teach.auto_eval
    prof.variables['observations'] = teach.observations
    prof.variables['pcp'] = teach.pcp
    prof.sedes = set(venue.id for venue in teach.venues.all())
    prof.set_mhor(teach.available_hours)
    prof.eval_self()

    return prof

# -----------------------------------------------------------------
def save_to_data_base(solc, django_clases, django_teachers):
    for (class_id, assig_tup) in solc.get_clprofs().items():
        current_class = django_clases.get(id=class_id)
        assigned_teacher = assig_tup[0]
        if assigned_teacher != 'nocand':
            current_class.teacher = django_teachers.get(id=assigned_teacher)
            current_class.save()


# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# Sin tener en cuenta el programa
esc = Escuela("Sabra el putas")

# Fetch all clases, cast them and put them into esc
django_clases = Class.objects.all()
for dc in django_clases:
    esc.add_clase(cast_class(dc))

django_courses = Course.objects.all()
for dc in django_courses:
    esc.add_curso(dc)

django_teachers = Teacher.objects.all()
for dt in django_teachers:
    esc.add_prof(cast_teacher(dt))

esc.assign_cands()

a = gen_rndsol(esc)
save_to_data_base(a, django_clases, django_teachers)
