import clase as cl, horario as hr, profesor as pr, curso as cr, random as rnd, time as tm
from escuela import Escuela

# cursos = {}
# clases = {}
# profesores = {}

# horarios = []



def gen_rstr(size, prefix=""):
    a = prefix
    for i in range(size):
        a += rnd.choice(letters)
    return a


def gen_rnum(size, prefix=""):
    a = prefix
    for i in range(size):
        a += str(rnd.randint(0, 1))
    return a


def gen_courses(esc):
    # gen bas a1
    for lvl in range(1, 6):
        if lvl <= 3:
            for let in ["A", "B", "C"]:
                curso = cr.Curso(str(lvl) + let)
                curso.add_reqr("enga1")
                esc.add_curso(curso)

            else:
                curso = cr.Curso(str(lvl))
                curso.add_reqr("enga1")
                esc.add_curso(curso)
    # gen a2
    for lvl in range(6, 11):
        curso = cr.Curso(str(lvl))
        curso.add_reqr("enga2")
        esc.add_curso(curso)

    # gen b1
    for lvl in range(11, 15):
        curso = cr.Curso(str(lvl))
        curso.add_reqr("engb1")
        esc.add_curso(curso)

    # gen b2
    for lvl in range(15, 20):
        if lvl == 19:
            for let in ["A", "B", "C", "D"]:
                curso = cr.Curso("19" + let)
                curso.add_reqr("engb2")
                esc.add_curso(curso)
            else:
                curso = cr.Curso(str(lvl))
                curso.add_reqr("engb2")
                esc.add_curso(curso)


def create_clase(dias, horas, sede, clase_ind, curso):
    clase = cl.Clase(curso + sede + str(clase_ind), curso, sede)
    clase.set_horario(dias, horas)
    return clase


def gen_clases(esc):
    # not very elegant but good for readability
    for (curso, _) in esc.get_cursos().items():
        # CURSOS CON HORARIO REGULAR
        clase_ind = 0

        # l y w
        dias = ["l", "w"]
        # for now lets ignore those halves ye?
        # 18.30 a 20.30
        horas = [18, 19]
        # sede poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # sede laureles
        esc.add_clase(create_clase(dias, horas, "l", clase_ind, curso))
        clase_ind += 1

        # m y j
        dias = ["m", "j"]

        # 10 a 12 poblado
        horas = [10, 11]
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # 12 a 2 pm poblado
        horas = [12, 13]
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # 6.30 a 8.30 poblado
        horas = [18, 19]
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # misma hora laureles y sede sur
        esc.add_clase(create_clase(dias, horas, "l", clase_ind, curso))
        clase_ind += 1

        esc.add_clase(create_clase(dias, horas, "s", clase_ind, curso))
        clase_ind += 1

        # miercoles y viernes
        dias = ["w", "v"]
        # 12 a 2
        horas = [12, 13]
        # sede sur
        esc.add_clase(create_clase(dias, horas, "s", clase_ind, curso))
        clase_ind += 1

        # THERE IS A SCHEDULE WITH DIFFERENT HOURS
        # DEPENDING ON THE DAY SO FIGURE THAT OUT
        # viernes 6.30 a 8.30, sabado 8 am a 10 am

        # sabado
        dias = ["s"]
        # de 8 am a 12 am
        horas = [8, 9, 10, 11]

        # sede poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # sede belen
        esc.add_clase(create_clase(dias, horas, "b", clase_ind, curso))
        clase_ind += 1

        # sede llanogrande
        esc.add_clase(create_clase(dias, horas, "r", clase_ind, curso))
        clase_ind += 1

        # de 1pm a 5pm
        horas = [13, 14, 15, 16]
        # sede poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # sede laureles
        esc.add_clase(create_clase(dias, horas, "l", clase_ind, curso))
        clase_ind += 1

        # CURSOS SEMI INTENSIVOS
        dias = ["l", "w", "v"]
        # de 6 a 8 am
        horas = [6, 7]

        # sede poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # sede laureles
        esc.add_clase(create_clase(dias, horas, "l", clase_ind, curso))
        clase_ind += 1

        # de 12 a 2 pm
        horas = [12, 13]

        # sede poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # sede sur
        esc.add_clase(create_clase(dias, horas, "s", clase_ind, curso))
        clase_ind += 1

        # de 10 a 12 am
        horas = [10, 11]

        # poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # de 6.30 a 8.30 pm
        horas = [18, 19]

        # sede sur
        esc.add_clase(create_clase(dias, horas, "s", clase_ind, curso))
        clase_ind += 1

        # marts y jueves
        dias = ["m", "j"]

        # 6 a 9 am
        horas = [6, 7, 8]

        # sede poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # sede laureles
        esc.add_clase(create_clase(dias, horas, "l", clase_ind, curso))
        clase_ind += 1

        # sede sur
        esc.add_clase(create_clase(dias, horas, "s", clase_ind, curso))
        clase_ind += 1

        # 9 a 12 m
        horas = [9, 10, 11]

        # sede poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # sede sur
        esc.add_clase(create_clase(dias, horas, "s", clase_ind, curso))
        clase_ind += 1

        # miercoles y viernes
        dias = ["w", "v"]

        # 6 a 9
        horas = [6, 7, 8]

        # sede poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # 9 a 12
        horas = [9, 10, 11]

        # poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # laureles
        esc.add_clase(create_clase(dias, horas, "l", clase_ind, curso))
        clase_ind += 1

        # CURSOS INTENSIVOS

        # l m w j v
        dias = ["l", "m", "w", "j", "v"]

        # 6 a 8 am
        horas = [6, 7]

        # sede poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # sede sur
        esc.add_clase(create_clase(dias, horas, "s", clase_ind, curso))
        clase_ind += 1

        # 8 a 10 am
        horas = [8, 9]

        # sede poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # sede laureles
        esc.add_clase(create_clase(dias, horas, "l", clase_ind, curso))
        clase_ind += 1

        # 10 a 12 am
        horas = [10, 11]

        # sede poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # 12 a 2 pm
        horas = [12, 13]

        # sede poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # dias l m w j
        dias = ["l", "m", "w", "j"]

        # 6.30 a 9
        horas = [6, 7, 8]

        # sede poblado
        esc.add_clase(create_clase(dias, horas, "u", clase_ind, curso))
        clase_ind += 1

        # sede laureles
        esc.add_clase(create_clase(dias, horas, "l", clase_ind, curso))
        clase_ind += 1

        # sede sur
        esc.add_clase(create_clase(dias, horas, "s", clase_ind, curso))
        clase_ind += 1


def get_esc_sch(esc):
    class_schs = []
    clases = esc.get_clases()
    for clase in clases.values():
        hor_clase = clase.get_horario()
        included = False
        for sch in class_schs:
            if hor_clase.equal_to(sch):
                included = True
                break
        if not included:
            class_schs.append(hor_clase)
    print("there are", len(class_schs), "class schs")
    return class_schs


def gen_rnd_hor(prof, max_h):
    tot_h2 = max_h
    # print("max_h", max_h)
    while tot_h2 > 0:
        # print("tot_h", tot_h2)
        # print(prof.horario)
        for dia in ["l", "m", "w", "j", "v", "s"]:
            num_hours = rnd.randint(0, 8)
            tot_h2 -= num_hours
            if tot_h2 <= 0:
                break
            start = rnd.randint(6, 22 - num_hours)
            day_sch = []
            while num_hours > 0:
                day_sch.append(start)
                start += 1
                num_hours -= 1
            prof.set_avail([dia], day_sch)
    return tot_h2




def gen_rand_profs(amount, certper, sedper, classper, variables, sedes, esc):
    all_schs = get_esc_sch(esc)
    full_schs = 0
    hr_avg = 0
    certs_cat = ["enga1", "enga2", "engb1", "engb2"]

    for iden in range(amount):
        max_h = rnd.randint(22, 39)
        # max_h = 0
        prof = pr.Profesor(iden, max_horas = max_h)

        # print(prof.get_horario())
        sch_amount = 0
        for esc_sch in all_schs:
            roll = rnd.random()
            # print(roll)
            if roll < classper:
                sch_amount+=1
                prof.copy_avail_sch(esc_sch)
        
        
        # # every professor will be able to teach 75% of
        # the cpurses
        for reqr in certs_cat:
            if rnd.random() < certper:
                prof.add_reqr(reqr)

        # assign some variables
        for var in prof.variables:
            roll = rnd.random()
            if roll < 0.2:
                prof.set_var(var, rnd.randint(0, 1))
            elif roll < 0.9:
                prof.set_var(var, rnd.randint(2, 4))
            else:
                prof.set_var(var, 5)

        # available in all locations
        for sede in sedes:
            if rnd.random() < sedper:
                prof.add_sede(sede)

        prof.eval_self()
        # print(len(prof.reqr))
        # print(prof.horario)
        esc.add_prof(prof)

    # assign candidates
    

def assign_cands(esc):
    clases = esc.get_clases().values()
    profesores = esc.get_profs().values()
    for clase in clases:
        for prof in profesores:
            if clase.can_teach(prof, esc):
                clase.add_cand(prof)
                # print("HIFIFIFIIFIFI")

        # SORT CANDIDATE TEACHERS BY SCORE
        clase.sort_cands(esc)
        
        # for cand in clase.get_cands():
        #     print(clase.eval_prof(esc.get_prof(cand)))
        # # print(len(clase.candidates))

    # for p2 in profesores:
    #     p = profesores[p2]
    #     # print(p.horario.count_avail())


def gen_rndesc(prof_amount, certper, sedper, claseper, variabs, sedes):
    rnd_esc = Escuela("rnd_esc");
    gen_courses(rnd_esc)
    # print("there are", len(rnd_esc.get_cursos()), "courses")
    gen_clases(rnd_esc)
    # print("there are", len(rnd_esc.get_clases()), "clases")
    gen_rand_profs(prof_amount, certper, sedper, claseper, variabs, sedes, rnd_esc)
    # print("there are", len(rnd_esc.get_profs()), "profs")    
    assign_cands(rnd_esc)
    return rnd_esc
# courses = gen_courses()
# print("number of courses", len(courses))
# print("number of clases", len(gen_clases(courses)))
# print("number of teachers", len(gen_rand_profs(400)))
