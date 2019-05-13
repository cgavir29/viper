import clase as cl
import curso as cr
import profesor as pr

class Escuela:
    def __init__(self, name, max_score = 0 ):
        self.max_score = max_score
        self.name = name
        null_prof = pr.Profesor("nocand");
        null_prof.set_var("nocand", -1000);
        self.profs = {"nocand": null_prof}
        self.clases = {}
        self.cursos = {}

    def print_info(self):
        print("there are", len(self.cursos), "courses")
        print("there are", len(self.clases), "clases")
        print("there are", len(self.profs), "profs")
        avg_avail = 0
        avg_occ = 0
        avg_max = 0
        for prof in self.profs.values():
            avg_avail+=prof.get_horario().count_avail()
            avg_occ+= prof.get_horario().get_total_h()
            avg_max+= prof.get_mhor()

            
        print("avg avail is", avg_avail/len(self.profs))
        print("avg occupied is", avg_occ/len(self.profs))
        print("avg max is", avg_max/len(self.profs))

        cands = [len(x.get_cands()) for x in self.clases.values()]
        print("avg num of cands is", sum(cands)/len(cands), "\n")
        
                        
        
    def get_profs(self):
        return self.profs

    def get_prof(self, profid):
        val = self.profs.get(profid)
        if val == None:
            print(profid)
            print(self.profs)
        return val

    def add_prof(self, prof):
        self.profs[prof.get_id()] = prof

    def get_clases(self):
        return self.clases

    def get_clase(self, claseid):
        return self.clases.get(claseid)

    def add_clase(self, clase):
        self.clases[clase.get_id()] = clase

    def get_cursos(self):
        return self.cursos

    def get_curso(self, cursoid):
        return self.cursos.get(cursoid)

    def add_curso(self, curso):
        self.cursos[curso.get_id()] = curso
    
