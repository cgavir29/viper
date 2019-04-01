import clase as cl, horario as hr, profesor as pr, curso as cr, random as rnd, time as tm

# cursos = {}
# clases = {}
# profesores = {}

# horarios = []

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
strdias = "lmwjv"
sedes = ["u", "s", "l", "b", "r", "p"]

certs_cat = ["enga1", "enga2", "engb1", "engb2"]


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


def gen_courses():
    # gen bas a1
    cursos = {}
    for lvl in range(1, 6):
        if lvl <= 3:
            for let in ["A", "B", "C"]:
                curso = cr.Curso(str(lvl) + let)
                curso.add_reqr("enga1")
                cursos[curso.iden] = curso
            else:
                curso = cr.Curso(str(lvl))
                curso.add_reqr("enga1")
                cursos[curso.iden] = curso
    # gen a2
    for lvl in range(6, 11):
        curso = cr.Curso(str(lvl))
        curso.add_reqr("enga2")
        cursos[curso.iden] = curso
    # gen b1
    for lvl in range(11, 15):
        curso = cr.Curso(str(lvl))
        curso.add_reqr("engb1")
        cursos[curso.iden] = curso
    # gen b2
    for lvl in range(15, 20):
        if lvl == 19:
            for let in ["A", "B", "C", "D"]:
                curso = cr.Curso("19" + let)
                curso.add_reqr("engb2")
                cursos[curso.iden] = curso
            else:
                curso = cr.Curso(str(lvl))
                curso.add_reqr("engb2")
                cursos[curso.iden] = curso
    return cursos


def gen_courses_tiny():
    # gen bas a1
    cursos = {}
    for lvl in range(1, 3):
        curso = cr.Curso(str(lvl))
        curso.add_reqr("enga1")
        cursos[curso.iden] = curso

    for lvl in range(15, 16):
        curso = cr.Curso(str(lvl))
        curso.add_reqr("engb2")
        cursos[curso.iden] = curso
    return cursos


def create_clase(dias, horas, sede, clase_ind, curso, clases):
    clase = cl.Clase(curso.iden + sede + str(clase_ind), curso, sede)
    clase.set_dias(dias, horas)
    clases[clase.iden] = clase


def gen_clases(cursos):
    clases = {}
    # not very elegant but good for readability
    for cursoid in cursos:
        curso = cursos[cursoid]
        # CURSOS CON HORARIO REGULAR
        clase_ind = 0

        # l y w
        dias = ["l", "w"]
        # for now lets ignore those halves ye?
        # 18.30 a 20.30
        horas = [18, 19]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede laureles
        create_clase(dias, horas, "l", clase_ind, curso, clases)
        clase_ind += 1

        # m y j
        dias = ["m", "j"]
        # 12 a 2 pm poblado
        horas = [12, 13]
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # 6.30 a 8.30 poblado
        horas = [18, 19]
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # THERE IS A SCHEDULE WITH DIFFERENT HOURS
        # DEPENDING ON THE DAY SO FIGURE THAT OUT
        # viernes 6.30 a 8.30, sabado 8 am a 10 am

        # sabado
        dias = ["s"]
        # de 8 am a 12 am
        horas = [8, 9, 10, 11]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede belen
        create_clase(dias, horas, "b", clase_ind, curso, clases)
        clase_ind += 1

        # sede llanogrande
        create_clase(dias, horas, "r", clase_ind, curso, clases)
        clase_ind += 1

        # CURSOS SEMI INTENSIVOS
        dias = ["l", "w", "v"]
        # de 6 a 8 am
        horas = [6, 7]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede laureles
        create_clase(dias, horas, "l", clase_ind, curso, clases)
        clase_ind += 1

        # de 6.30 a 8.30 pm
        horas = [18, 19]

        # sede sur
        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

        # 9 a 12 m
        horas = [9, 10, 11]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede sur
        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

        # CURSOS INTENSIVOS

        # l m w j v
        dias = ["l", "m", "w", "j", "v"]

        # 6 a 8 am
        horas = [6, 7]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede sur
        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

        # 10 a 12 am
        horas = [10, 11]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # 12 a 2 pm
        horas = [12, 13]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # dias l m w j
        dias = ["l", "m", "w", "j"]

        # 6.30 a 9
        horas = [6, 7, 8]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede laureles
        create_clase(dias, horas, "l", clase_ind, curso, clases)
        clase_ind += 1

        # sede sur
        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

    return clases
    # print(clase_ind)


def gen_clases_full():
    clases = {}
    # not very elegant but good for readability
    for cursoid in cursos:
        curso = cursos[cursoid]
        # CURSOS CON HORARIO REGULAR
        clase_ind = 0

        # l y w
        dias = ["l", "w"]
        # for now lets ignore those halves ye?
        # 18.30 a 20.30
        horas = [18, 19]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede laureles
        create_clase(dias, horas, "l", clase_ind, curso, clases)
        clase_ind += 1

        # m y j
        dias = ["m", "j"]

        # 10 a 12 poblado
        horas = [10, 11]
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # 12 a 2 pm poblado
        horas = [12, 13]
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # 6.30 a 8.30 poblado
        horas = [18, 19]
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # misma hora laureles y sede sur
        create_clase(dias, horas, "l", clase_ind, curso, clases)
        clase_ind += 1

        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

        # miercoles y viernes
        dias = ["w", "v"]
        # 12 a 2
        horas = [12, 13]
        # sede sur
        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

        # THERE IS A SCHEDULE WITH DIFFERENT HOURS
        # DEPENDING ON THE DAY SO FIGURE THAT OUT
        # viernes 6.30 a 8.30, sabado 8 am a 10 am

        # sabado
        dias = ["s"]
        # de 8 am a 12 am
        horas = [8, 9, 10, 11]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede belen
        create_clase(dias, horas, "b", clase_ind, curso, clases)
        clase_ind += 1

        # sede llanogrande
        create_clase(dias, horas, "r", clase_ind, curso, clases)
        clase_ind += 1

        # de 1pm a 5pm
        horas = [13, 14, 15, 16]
        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede laureles
        create_clase(dias, horas, "l", clase_ind, curso, clases)
        clase_ind += 1

        # CURSOS SEMI INTENSIVOS
        dias = ["l", "w", "v"]
        # de 6 a 8 am
        horas = [6, 7]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede laureles
        create_clase(dias, horas, "l", clase_ind, curso, clases)
        clase_ind += 1

        # de 12 a 2 pm
        horas = [12, 13]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede sur
        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

        # de 10 a 12 am
        horas = [10, 11]

        # poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # de 6.30 a 8.30 pm
        horas = [18, 19]

        # sede sur
        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

        # marts y jueves
        dias = ["m", "j"]

        # 6 a 9 am
        horas = [6, 7, 8]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede laureles
        create_clase(dias, horas, "l", clase_ind, curso, clases)
        clase_ind += 1

        # sede sur
        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

        # 9 a 12 m
        horas = [9, 10, 11]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede sur
        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

        # miercoles y viernes
        dias = ["w", "v"]

        # 6 a 9
        horas = [6, 7, 8]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # 9 a 12
        horas = [9, 10, 11]

        # poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # laureles
        create_clase(dias, horas, "l", clase_ind, curso, clases)
        clase_ind += 1

        # CURSOS INTENSIVOS

        # l m w j v
        dias = ["l", "m", "w", "j", "v"]

        # 6 a 8 am
        horas = [6, 7]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede sur
        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

        # 8 a 10 am
        horas = [8, 9]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede laureles
        create_clase(dias, horas, "l", clase_ind, curso, clases)
        clase_ind += 1

        # 10 a 12 am
        horas = [10, 11]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # 12 a 2 pm
        horas = [12, 13]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # dias l m w j
        dias = ["l", "m", "w", "j"]

        # 6.30 a 9
        horas = [6, 7, 8]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # sede laureles
        create_clase(dias, horas, "l", clase_ind, curso, clases)
        clase_ind += 1

        # sede sur
        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

    return clases
    # print(clase_ind)

def gen_clases_tiny(cursos):
    clases = {}
    # not very elegant but good for readability
    for cursoid in cursos:
        curso = cursos[cursoid]
        # CURSOS CON HORARIO REGULAR
        clase_ind = 0

        # l y w
        dias = ["l", "w"]
        # for now lets ignore those halves ye?
        # 18.30 a 20.30
        horas = [18, 19]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # m y j
        dias = ["m", "j"]
        # 12 a 2 pm poblado
        horas = [12, 13]
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # THERE IS A SCHEDULE WITH DIFFERENT HOURS
        # DEPENDING ON THE DAY SO FIGURE THAT OUT
        # viernes 6.30 a 8.30, sabado 8 am a 10 am

        # sabado
        dias = ["s"]
        # de 8 am a 12 am
        horas = [8, 9, 10, 11]

        # sede belen
        create_clase(dias, horas, "b", clase_ind, curso, clases)
        clase_ind += 1

        # CURSOS SEMI INTENSIVOS
        dias = ["l", "w", "v"]
        # de 6 a 8 am
        horas = [6, 7]

        # sede laureles
        create_clase(dias, horas, "l", clase_ind, curso, clases)
        clase_ind += 1

        # de 6.30 a 8.30 pm
        horas = [18, 19]

        # sede sur
        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

        # 9 a 12 m
        horas = [9, 10, 11]

        # sede sur
        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

        # CURSOS INTENSIVOS

        # l m w j v
        dias = ["l", "m", "w", "j", "v"]

        # 6 a 8 am
        horas = [6, 7]

        # sede sur
        create_clase(dias, horas, "s", clase_ind, curso, clases)
        clase_ind += 1

        # 10 a 12 am
        horas = [10, 11]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # 12 a 2 pm
        horas = [12, 13]

        # sede poblado
        create_clase(dias, horas, "u", clase_ind, curso, clases)
        clase_ind += 1

        # dias l m w j
        dias = ["l", "m", "w", "j"]

        # 6.30 a 9
        horas = [6, 7, 8]

        # sede laureles
        create_clase(dias, horas, "l", clase_ind, curso, clases)
        clase_ind += 1

    return clases


def gen_rnd_hor(prof, max_h):
    tot_h = max_h
    while tot_h > 0:
        for dia in ["l", "m", "w", "j", "v", "s"]:
            num_hours = rnd.randint(0, 8)
            tot_h -= num_hours
            if tot_h <= 0: break
            start = rnd.randint(6, 22)
            day_sch = []
            while num_hours > 0:
                day_sch.append(start)
                start += 1
                num_hours -= 1
            prof.set_avail([dia], day_sch)
    return tot_h
def gen_rand_profs(amount, clases, certper, sedper, rndsch=False):
    profesores = {}
    full_schs = 0
    hr_avg = 0
    for i in range(amount):
        this_iden = i
        prof = pr.Profesor(this_iden)

        # initially, teachrs have a full day schedule
        # from 6 am to 9pm nigga
        if not rndsch:
            prof.set_avail(["l", "m", "w", "j", "v", "s"], [c for c in range(6, 22)])
        else:
            hr_len = rnd.randint(23, 38)
            hr_avg += hr_len - gen_rnd_hor(prof, hr_len)
        # every professor will be able to teach 75% of
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
        for sed in sedes:
            if rnd.random() < sedper:
                prof.sedes[sed] = 1

        prof.eval_self()
        # print(len(prof.reqr))
        profesores[prof.iden] = prof

    # assign candidates
    ini = tm.time()
    for claid in clases:
        clase = clases[claid]
        for profid in profesores:
            prof = profesores[profid]
            if clase.can_teach(prof):
                # print("teacher assigned")
                clase.add_cand(prof)

        # SORT CANDIDATE TEACHERS BY SCORE
        clase.candidates = sorted(clase.candidates, key=lambda a: a[1], reverse=True)
        # print(len(clase.candidates))

    # for p2 in profesores:
    #     p = profesores[p2]
    #     # print(p.horario.count_avail())
    print("candidates assigned in", tm.time() - ini)
    print("avg num of hrs is", hr_avg / amount)
    print("wow,", full_schs, "full schedules")

    return profesores


# courses = gen_courses()
# print("number of courses", len(courses))
# print("number of clases", len(gen_clases(courses)))
# print("number of teachers", len(gen_rand_profs(400)))
