import horario as hr
class Clase:
    def __init__(self, iden=None, curso=None, sede=None):
        self.iden = iden
        self.curso = curso
        self.sede = sede
        self.horario = hr.Horario()
        self.profesor = None
        self.candidates = []

    def __repr__(self):
        return f"clase: {self.iden}"

    def eval_prof(self, prof):
        #this whole thing is commented
        #because it may be that the function
        #only uses the variables in prof, but
        #it might change in the future
        
        #consider last hour in the same day
        # score = prof.horario_p.total_h
        # score = 0
        # for var in prof.variables:
        #     score+=prof.variables[var]

        # prof.score = score
        # return score
        return prof.score

    def can_teach(self, prof):
        if prof.sedes[self.sede]!=1:
            # print(prof.iden, "doesnt have the sede for", self.iden)
            return False
        
        if not prof.is_avail(self.horario):
            # print(prof.iden, "doesnt have the horario for", self.iden)  
            return False
        
        for r in self.curso.reqr:
            
            if prof.reqr.get(r) == None:
                # print(prof.iden, "doesnt have the reqr for", self.iden)            
                return False
        return True

    def set_prof(self, prof):
        self.profesor = prof.iden

    def add_cand(self, prof):
        self.candidates.append((prof.iden,self.eval_prof(prof)))

    def set_dias(self, dias, horas):
        for dia in dias:
            self.horario.set_horario(dia, horas, self.iden)

            
