class Solucion:
    def __init__(self):
        self.iden = None

        #we have these because each solution will have a COPY
        #of the objects

        #theres no add or delete methods because
        #both teachers and classes should be the same
        #for every solution
        # self.clases = {}
        #hash de tuplas (prof, numclases)
        self.profs = {}

        #hash de tuplas (profid, puntaje)
        #i will not delete the score from here even if i
        #have teacher score and numclasses
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


    def __repr__(self):
        return str(self.clase_prof)

    def get_prof(self, profid):
        tup = self.profs.get(profid)
        if tup != None: 
            return tup[0]

    # def get_clase(self, claseid):
    #     return self.clases.get(claseid)        


    def add_prof(self, prof):
        self.profs[prof.iden] = [prof, 0]
        
    def get_clprof(self, claseid):
        return self.clase_prof.get(claseid)

    def del_clprof(self, clase):
        tup = self.get_clprof(clase.iden)

        if tup != None:
            self.score -= tup[1]
            # print("THERE'S A GUY IN HERE!")
            #remove the class from the teacher too
            # num_h = self.profs.get(tup[0])[0].horario
            self.profs.get(tup[0])[0].del_clase(clase)
            self.profs.get(tup[0])[1] -= 1
            self.clase_prof[clase.iden] = None
            
            if self.profs.get(tup[0])[1] <= 0:
                self.active_profs-=1
                
        self.clase_prof[clase.iden] = None


    def set_clprof(self, clase, profid):

        #get both objects
        prof = self.get_prof(profid)
        
        #get score pasado
        tup = self.get_clprof(clase.iden)

        self.del_clprof(clase)

        #THE PROFESOR IS NOT ADDED TO THE profs THING HERE
        #IT IS ADDED WITH A ZERO IF IT WASNT PRESENT
        #WE MERELY INCREMENT IT
        
        self.profs[profid][1] += 1
        if self.profs[profid][1] == 1:
            self.active_profs+=1
        
        #get the score and add it
        punt =  clase.eval_prof(prof)
        self.score += punt
        self.clase_prof[clase.iden] = (profid, punt)

        #finally, add the class to the profesor
        prof.add_clase(clase)
        

            
        
