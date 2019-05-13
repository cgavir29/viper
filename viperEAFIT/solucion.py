import profesor as pr


class Solucion:
    def __init__(self):
        # we have these because each solution will have a COPY
        # of the objects

        # theres no add or delete methods because
        # both teachers and classes should be the same
        # for every solution
        # self.clases = {}
        # hash de tuplas (prof, numclases)
        null_prof = pr.Profesor("nocand")
        null_prof.set_var("nocand", -1000)

        self.profs = {"nocand": [null_prof, 1]}

        # hash de tuplas (profid, puntaje)
        # i will not delete the score from here even if i
        # have teacher score and numclasses
        """
        1. it might be that at some point the score will 
        also depend on class parameters
        
        2. it might be that at some point it is forced to assign
        a class to a teacher even if its score is 0 for that parti-
        cular class
        """
        self.clase_prof = {}
        self.score = 0
        self.active_profs = 0
        self.nom_score = 0
        self.holes = set()
        self.under_assigned = 0

    def __repr__(self):
        return str(self.clase_prof)

    def print_asigs(self, esc):
        for (clasid, asig_tup) in self.clase_prof.items():
            clase = esc.get_clase(clasid)
            prof = champ_sol.get_prof(asig_tup[0])
            prof_og = esc.get_prof(asig_tup[0])

            print("CLASS-----------------------------")
            print(clase.get_horario(), "\n")
            print("PROF------------------------------")
            print(prof.get_horario())
            print(prof.get_horario().get_total_h())
            print("PROF ORIG-------------------------")
            print(prof_og.get_horario())
            print(prof_og.get_horario().get_total_h())

    def get_prof(self, profid):
        tup = self.profs.get(profid)
        if tup != None:
            return tup[0]
        else:
            return None

    def get_score(self):
        return self.score

    def get_actprofs(self):
        return self.active_profs

    def get_profs(self):
        return self.profs

    def get_num_clases(self, profid):
        tup = self.profs.get(profid)
        if tup != None:
            return tup[1]
        else:
            return None

    def add_prof(self, prof):
        self.profs[prof.iden] = [prof.copy_self(), 0]

    def get_clprofs(self):
        return self.clase_prof

    def get_clprof(self, claseid):
        return self.clase_prof.get(claseid)

    def del_clprof(self, clase):
        tup = self.get_clprof(clase.get_id())

        if tup != None:
            local_sod = self.profs.get(tup[0])[0]
            self.score -= tup[1]
            self.nom_score -= local_sod.get_score()
            # print("THERE'S A GUY IN HERE!")
            # remove the class from the teacher too
            # num_h = self.profs.get(tup[0])[0].horario
            local_sod.del_clase(clase)

            self.profs.get(tup[0])[1] -= 1
            self.clase_prof.pop(clase.get_id(), None)

            if self.profs.get(tup[0])[1] == 0:
                self.active_profs -= 1

        self.clase_prof.pop(clase.get_id(), None)

    def set_clprof(self, clase, profid):
        if profid == "nocand":
            self.add_hole(clase)
        else:
            self.del_clprof(clase)
            self.del_hole(clase)

            # THE PROFESOR IS NOT ADDED TO THE profs THING HERE
            # IT IS ADDED WITH A ZERO IF IT WASNT PRESENT
            # WE MERELY INCREMENT IT

            prof = self.get_prof(profid)
            self.profs[profid][1] += 1
            if self.profs[profid][1] == 1:
                self.active_profs += 1

            # get the score and add it
            punt = clase.eval_prof(prof)
            self.score += punt
            self.clase_prof[clase.iden] = [profid, punt]

            # finally, add the class to the profesor
            prof.add_clase(clase)
            self.nom_score += prof.get_score()

    def get_holes(self):
        return self.holes

    def add_hole(self, clase):
        self.del_clprof(clase)
        self.clase_prof[clase.get_id()] = ["nocand", 0]
        self.holes.add(clase.get_id())

    def del_hole(self, clase):
        if clase.get_id() in self.holes:
            self.holes.remove(clase.get_id())

    def has_hole(self, clase):
        return clase.get_id() in self.holes

    def count_holes(self):
        count = 0
        for (asig, _) in self.clase_prof.values():
            if asig == "nocand":
                count += 1
        return count

    def conf_nom_score(self):
        rscore = 0
        for (asig, _) in self.clase_prof.values():
            prof = self.get_prof(asig)
            rscore += prof.get_score()

        return rscore

    def print_to_file(self, filename):
        f = open(filename, "w")
        for i in self.profs.values():
            output = "\n" + str(i[0].iden) + "\n" + str(i[0].horario)
            f.write(output)

    def print_info(self):
        num_act_profs = 0
        for prof in self.profs.values():
            if prof[1] != 0:
                num_act_profs += 1

        print("active profs", self.get_actprofs(), "conf", num_act_profs)
        print("score", self.get_score())
        print("holes", len(self.get_holes()), "conf", self.count_holes())
        unis = 0
        average = 0
        for (prof, num) in self.get_profs().values():
            if prof.get_id() == "nocand":
                continue
            num_h = prof.get_horario().get_total_h()
            if num_h < 20:
                unis += 1

            average += num_h

        print("nominal score", self.nom_score, "conf", self.conf_nom_score())

<<<<<<< HEAD
        print("average num of h", average / self.active_profs)
        print(unis, "under used teachers\n")
=======
        print("average num of h", average/self.active_profs)        
        #print(unis, "under used teachers\n")
>>>>>>> 251e2d8de869e67d39a82425c8d2787f5d59377c
