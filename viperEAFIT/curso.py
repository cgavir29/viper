class Curso:
    def __init__(self, iden):
        self.iden = iden

        #si solo se requiere el certificado que indica que tiene
        #permiso para dictar el curso, poner esa info en el nombre
        
        self.reqr = set() #certificados necesarios para un curso
                       #por ejemplo, c2 en ingles, etc

        """Si se implementar variables aqui, suponemos que hay
        una funcion de evaluacion ligeramente distinta entre 
        los diferentes cursos, por ejemplo, que alguno valora
        microteaching mas que otro"""
        
        # self.variables = {} #posiblemente deje de existir y serán
        #                     #funciones y valores fijos
                
    def __repr__(self):
        return f'curso: {self.iden}'

    def get_id(self):
        return self.iden

    def set_id(self, new_id):
        self.iden = new_id
        
    def add_reqr(self, reqr):
        self.reqr.add(reqr);

    def get_reqr(self):
        return self.reqr
        
        
    

    #may dissapear along with variables
    # def add_var(self, var, val):
    #     self.variables[var] = val

        

