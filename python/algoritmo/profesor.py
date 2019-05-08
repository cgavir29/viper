import clase as cl
from horario import Horario


class Profesor:
    def __init__(self, iden, horario=None, score=0, max_horas=0):
        self.iden = iden
        self.horario = Horario()
        # self.horario_p = hr.Horario()  # horario
        # corresponde a los llamados "cursos aprobados"
        self.reqr = set()

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
            "estatus": 0,
        }

        self.sedes = set()

        self.max_horas = max_horas
        # los cursos que el profesor esta dictando, por ejemplo
        # ingles para niños c1 etc...
        # importante para la regla de maximo 4 asignaturas
        # y la repeticion
        # modificado por set_prof
        # self.cursos = {}
        # si es pereira no asignar dos sedes minimo
        # this works as long as the function ONLY uses the variables
        self.score = score

    def __repr__(self):
        return f"pr{self.iden}"

    def get_id(self):
        return self.iden

    def get_horario(self):
        return self.horario

    def eval_self(self):
        score = 0.0
        for var in self.variables.keys():
            score += self.variables.get(var)

        self.score = score

    def copy_self(self):
        prof = Profesor(self.get_id(), score=self.score, max_horas=self.max_horas)
        
        this_diario = self.get_horario().get_diario()
        for dia in this_diario.keys():
            hour_class = self.get_horario().get_dia(dia)
            for (hora, val) in hour_class.items():
                prof.get_horario().set_single(dia, hora, val)

        return prof

    def set_avail(self, dias, horas):
        for dia in dias:
            self.horario.set_horario(dia, horas, "0", True)

    def is_avail(self, horariocl):
        diario = horariocl.get_diario()
        for dia in diario.keys():
            horas = horariocl.get_dia(dia).keys()
            for hora in horas:
                if self.horario.get_horario(dia, hora) != "0":
                    # print(dia, hora, self.horario.get_horario(dia, hora))
                    return False
        return True

    def add_clase(self, clase):
        class_sch = clase.get_horario()

        for dia in class_sch.get_diario().keys():
            daily = class_sch.get_dia(dia)
            for (hora, clase) in daily.items():
                self.horario.set_single(dia, hora, clase)

    def del_clase(self, clase):
        class_sch = clase.get_horario()
        for dia in class_sch.get_diario().keys():
            daily = class_sch.get_dia(dia).keys()
            for hora in daily:
                self.horario.set_single(dia, hora, "0", False)

    def copy_avail_sch(self, hor):
        dias = hor.get_diario().keys()
        horas = []
        for dia in dias:
            for time in hor.get_dia(dia).keys():
                horas.append(time)
            self.horario.set_horario(dia, horas, "0", True)



    def get_reqr(self):
        return self.reqr

    def add_reqr(self, reqr):
        self.reqr.add(reqr)

    def get_vars(self):
        return self.variables

    def set_var(self, key, val):
        self.variables[key] = val

    def get_var(self, key):
        return self.variables[key]
    
    def get_sedes(self):
        return self.sedes

    def add_sede(self, sede):
        self.sedes.add(sede)

    def get_mhor(self):
        return self.max_horas

    def set_mhor(self, val):
        self.max_horas = val
        
    def get_score(self):
        return self.score

