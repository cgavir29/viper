# Django
from schedules.models import Schedule
from academics.models import Class, Course
from accounts.models import Teacher
# Own
from .escuela import Escuela
from .clase import Clase
from .horario import Horario
from .profesor import Profesor
from .lns import gen_rndsol
from .tester import run_pure_lns



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


    prof.variables['sufficiency'] = teach.sufficiency
    prof.variables['simevi'] = teach.simevi
    prof.variables['coor_eval'] = teach.coor_eval
    prof.variables['student_eval'] = teach.student_eval
    prof.variables['self_eval'] = teach.self_eval
    prof.variables['observations'] = teach.observations
    prof.variables['pdp'] = teach.pdp
    prof.sedes = set(venue.id for venue in teach.venues.all())
    prof.set_mhor(teach.available_hours)
    prof.eval_self()

    return prof

# -----------------------------------------------------------------
def save_to_data_base(solc, django_classes, django_teachers):
    for (class_id, assig_tup) in solc.get_clprofs().items():
        current_class = django_classes.get(id=class_id)
        assigned_teacher = assig_tup[0]
        if assigned_teacher != 'nocand':
            current_class.teacher = django_teachers.get(id=assigned_teacher)
            current_class.save()
            # quitar disponibilidad


# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
def run(program_name):
    esc = Escuela(program_name)
    
    # Add classes to escuela
    django_classes = Class.objects.all()
    for dc in django_classes:
        esc.add_clase(cast_class(dc))

    # Add courses to escuela
    django_courses = Course.objects.all()
    for dc in django_courses:
        esc.add_curso(dc)

    # Add teachers to escuela
    django_teachers = Teacher.objects.all()
    for dt in django_teachers:
        esc.add_prof(cast_teacher(dt))

    print('Clases', esc.get_clases())
    print('Courses', esc.get_cursos())
    print('Teachers', esc.get_profs())

    esc.assign_cands()

    for cl in esc.get_clases().values():
        print(cl.iden)
        
        print('Sede', cl.sede)
        print(cl.get_cands())
        print('Horario', cl.get_horario())
    sol = run_pure_lns(esc)
    print(sol.clase_prof)
    save_to_data_base(sol, django_classes, django_teachers)

    #sol = gen_rndsol(esc)
    #save_to_data_base(sol, django_classes, django_teachers)



