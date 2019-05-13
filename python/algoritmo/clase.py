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

    def get_id(self):
        return self.iden

    def get_sede(self):
        return self.sede

    def get_prof(self):
        if self.profesor:
            return self.profesor
        else:
            return "nocand"

    def set_prof(self, prof):
        self.profesor = prof.copy_self()

    def get_horario(self):
        return self.horario
    
    def set_horario(self, dias, horas):
        for dia in dias:
            self.horario.set_horario(dia, horas, self.iden, True)
 
    def change_cands(self, cands):
        self.candidates = cands

    def get_cands(self):
        return self.candidates

    def add_cand(self, prof):
        self.candidates.append(prof.get_id())
        
    def eval_prof(self, prof):
        score = 0.0
        
        if prof.is_overused():
            return 0.0
        
        score += prof.get_score()
        return score

    def sort_cands(self, esc):
        # for cand in self.candidates:
        #     print(cand)
        #     self.eval_prof(esc.get_prof(cand))
        
        temp_fn = lambda x: self.eval_prof(esc.get_prof(x))
        self.candidates.sort(key=temp_fn, reverse=True)
        
    def can_teach(self, prof, esc):
        
        if self.sede not in prof.get_sedes():
            # print(prof.iden, "doesnt have the sede for", self.iden)
            return False

        if not prof.has_sch(self.horario):
            # print(prof.iden, "doesnt have the horario for", self.iden)
            return False

        this_curso = esc.get_curso(self.curso)
        
        for r in this_curso.get_reqr():
            if r not in prof.get_reqr():
                # print(prof.iden, "doesnt have reqr for", self.iden)
                return False
            
        return True
