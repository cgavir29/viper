import clase as cl
from horario import Horario

class Prof_Base:
    def __init__(self, iden, score, max_horas, horario=None):

        if horario == None:
            self.horario = Horario()
        else:
            self.horario = horario

        self.id = iden
        self.score = score
        self.max_horas = max_horas

    def __repr__(self):
        return f"pr{self.id}"

    def get_id(self):
        return self.id

    def get_horario(self):
        return self.horario

    def copy_self(self):
        prof = Prof_Base(self.get_id(), self.score, self.max_horas)

        this_diario = self.get_horario().get_diario()
        for dia in this_diario.keys():
            hour_class = self.get_horario().get_dia(dia)
            for (hora, val) in hour_class.items():
                prof.get_horario().set_single(dia, hora, val)

        return prof

    def set_avail(self, dias, horas):
        for dia in dias:
            self.horario.set_horario(dia, horas, "0", True)

    def has_sch(self, horariocl):
        diario = horariocl.get_diario()
        for dia in diario.keys():
            horas = horariocl.get_dia(dia).keys()
            for hora in horas:
                if self.horario.get_horario(dia, hora) != "0":
                    return False
        return True

    def is_overused(self):
        return self.horario.get_total_h() >= self.max_horas

        
    def sede_check(self, cl, esc):
        """
        you need to check the one that ends one hour before and the one
        that ends just before it, this is because, if both are present
        then they both share a sede, but if only the latter is present,
        then it might be in a diferent sede. i dont need to check the 
        one that ends 2 hours before (first_hour-3) because this time
        allows for displacement
        
        """
        horariocl = cl.get_horario()
        diario = horariocl.get_diario()

        profcl = self.get_horario()
        for dia in diario.keys():
            horas = horariocl.get_dia(dia).keys()
            if len(horas):
                first_hour = min(horas)
                last_hour = max(horas) + 1
                for hora in range(first_hour - 2, first_hour):
                    prev_claseid = profcl.get_horario(dia, hora)
                    try: 
                        prev_clase_sede = esc.get_clase(prev_claseid).get_sede()
                    
                        if prev_clase_sede != cl.get_sede():
                           return False
                    except:
                        pass

                for hora in range(last_hour, last_hour + 2):
                    pos_claseid = profcl.get_horario(dia, hora)

                    try: 
                        pos_clase_sede = esc.get_clase(pos_claseid).get_sede()
                        if pos_clase_sede() != cl.get_sede():    
                            return False
                    except:
                        pass

        return True


    def sede_check_2(self, cl, esc):
        horariocl = cl.get_horario()
        diario = horariocl.get_diario()

        profcl = self.get_horario()
        for dia in diario.keys():
            horas = list(horariocl.get_dia(dia).keys())
            if len(horas):
                first_hour = horas[0]
                last_hour = horas[-1] +1

                if first_hour >= last_hour:
                    raise NameError("Class hours are not sorted")
                #previous to the class
                clase_2h_prev_id = profcl.get_horario(dia,first_hour-2)
                clase_2h_prev = esc.get_clase(clase_2h_prev_id)
                if clase_2h_prev != None: 
                    if clase_2h_prev.get_sede() != cl.get_sede():
                        return False

                clase_1h_prev_id = profcl.get_horario(dia,first_hour-1)
                clase_1h_prev = esc.get_clase(clase_1h_prev_id)
                if clase_1h_prev != None: 
                    if clase_1h_prev.get_sede() != cl.get_sede():
                        return False


                clase_1h_post_id = profcl.get_horario(dia,last_hour+1)
                clase_1h_post = esc.get_clase(clase_1h_post_id)
                if clase_1h_post != None: 
                    if clase_1h_post.get_sede() != cl.get_sede():
                        return False


                clase_2h_post_id = profcl.get_horario(dia,last_hour+2)
                clase_2h_post = esc.get_clase(clase_2h_post_id)
                if clase_2h_post != None: 
                    if clase_2h_post.get_sede() != cl.get_sede():
                        return False
                    
        return True
                

    def is_avail(self, cl, esc):
        # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA DONT FORGET THIS IFFFFFFFFFFFFFF
        prof_is_overused = self.is_overused()

        prof_is_avail = self.has_sch(cl.get_horario())
        
        # prof_in_time = self.sede_check_2(cl, esc)
        prof_in_time = self.sede_check_2(cl, esc)
        
        return (not prof_is_overused) and prof_is_avail and prof_in_time

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

    def get_mhor(self):
        return self.max_horas

    def set_mhor(self, val):
        self.max_horas = val

    def get_score(self):
        return self.score


class Profesor(Prof_Base):
    def __init__(self, iden, horario=None, score=0, max_horas=0):
        Prof_Base.__init__(self, iden, score, max_horas, horario)
        
        # Todos los cursos que puede dictar el profesor
        self.reqr = set()

        """Ocurre lo mismo que ocurre en curso, se ponen 
        los valores que un profesor tiene. Por ejemplo, un 
        profesor experimentado tendria {experiencia : 5}
        todos los profesores tendran las mismas variables
        pero con valores distintos"""

        # estatus 0 si novicio, 1 si docente, 2 si master
        self.variables = {
            #"simevi":5,
            #"pdp":2,
        }

        self.sedes = set()

        # los cursos que el profesor esta dictando, por ejemplo
        # ingles para niños c1 etc...
        # importante para la regla de maximo 4 asignaturas
        # y la repeticion
        # modificado por set_prof
        # self.cursos = {}
        # si es pereira no asignar dos sedes minimo
        # this works as long as the function ONLY uses the variables

    def eval_self(self):
        score = 0.0
        for var in self.variables.keys():
            score += self.variables.get(var)

        self.score = score

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
