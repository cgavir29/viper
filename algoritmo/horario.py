# import clase as cl

class Horario:
    def __init__(self):
        # Esto representa las diferentes franjas horarias de cada dia
        # franjas por dia por que se trata con horarios 7 a 19
        # si una franja esta ocupada, significa que se va a utilizar
        # esa hora

        self.diario = {
            "l": ({}),
            "m": ({}),
            "w": ({}),
            "j": ({}),
            "v": ({}),
            "s": ({}),
        }

        self.total_h = 0  # total horas en el horario
    
    def __repr__(self):
        string_rep = ""
        for i in self.diario:
            if len(self.diario.get(i)) > 0:
                string_rep+=i+str(self.diario.get(i))+"\n"
        return string_rep
       # return f' l:{self.diario["l"]} \n m: {self.diario["m"]} \n w: {self.diario["w"]} \n j: {self.diario["j"]} \n v: {self.diario["v"]} \n s: {self.diario["s"]}'



    def get_diario(self):
        #this should be a reference in rust
        return self.diario
    
    def count_avail(self):
       zeros = 0
       for d in self.diario:
           for h in self.diario[d]:
               if self.diario[str(d)][h] == 0:
                   zeros+=1
       return zeros

    def get_dia(self, dia):
        return self.diario.get(dia)

    
    def get_horario(self, dia, hora):
        # possibly add exception here
        # to avoid erroneous input
        return self.diario.get(dia).get(hora)

    # cambia el estado de  cierta hora en cierto dia en el horario
    # si state es 1, la clase se reserva
    # si state es 0, la clase de remueve
    def set_horario(self, dia, horas, val, state=1):
        if state:
            for h in horas:
                self.diario[dia][h] = val
                if val != 0: 
                    self.total_h += 1
        else:
            for h in horas:
                self.diario[dia][h] = 0
                self.total_h -= 1



