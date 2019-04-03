import clase as cl
import horario as hr


class Profesor:
    def __init__(self, iden, horario = hr.Horario(), score = 0):
        self.iden = iden

        self.horario = horario
        # self.horario_p = hr.Horario()  # horario

        # corresponde a los llamados "cursos aprobados"
        self.reqr = {}


        """Ocurre lo mismo que ocurre en curso, se ponen 
        los valores que un profesor tiene. Por ejemplo, un 
        profesor experimentado tendria {experiencia : 5}
        todos los profesores tendran las mismas variables
        pero con valores distintos"""

        # estatus 0 si novicio, 1 si docente, 2 si master
        self.variables = {
            "simevi": 0,
            "microteaching": 0,
            "promedio_eval": 0,
            "observaciones": 0,
            "pdp_cum": 0,
            "max_horas": 0,
            "estatus": 0,
        }

        # los cursos que el profesor esta dictando, por ejemplo
        # ingles para niños c1 etc...
        # importante para la regla de maximo 4 asignaturas
        # y la repeticion
        # modificado por set_prof
       # self.cursos = {}

        # si es pereira no asignar dos sedes minimo
        self.sedes = {"u": 0, "s": 0, "l": 0, "b": 0, "r": 0, "p": 0}

        #this works as long as the function ONLY uses the variables
        self.score = score

    def __repr__(self):
        return f"pr{self.iden}"

    def add_reqr(self, cert):
        self.reqr[cert] = 1

    def set_var(self, var, val):
        self.variables[var] = val



    def get_sch(self):
        return self.horario.get_diario()
    #this only works as long as the class has NOTHING
    #to do with the evaluation function, which seems
    #to be the case so far, OTHERWISE, make it so
    #copy_prof in ga_engine2 copies the parameters

    #this way you dont need to compute the part of the
    #function that uses the variables everytime
    def eval_self(self):
        #consider last hour in the same day
        # score = prof.horario_p.total_h
        score = 0
        for var in self.variables:
            score+=self.variables[var]
        self.score = score

        
        

        
    def set_avail(self, dias, horas):
        for dia in dias: 
            self.horario.set_horario(dia, horas, 0)

    def is_avail(self, horariocl):
        for dia in list(horariocl.diario.keys()):
            for hora in horariocl.diario.get(dia):
                if self.horario.get_horario(dia, hora) != 0:
                    return False
        return True

    # TODO:
    def add_clase(self, clase):
        # add one to the particular course
        # val = self.cursos.get(clase.curso.iden)
        # if val == None:
        #     self.cursos[clase.curso.iden] = 1
        # else:
        #     self.cursos[clase.curso.iden] += 1

        for dia in list(clase.horario.diario.keys()):
            self.horario.set_horario(dia, clase.horario.get_dia(dia), clase.iden)

    def del_clase(self, clase):
        # sub one from course
        
        # self.cursos[clase.curso.iden] -=1
        for dia in list(clase.horario.diario.keys()):
            self.horario.set_horario(dia, clase.horario.get_dia(dia), clase.iden, state=0)
