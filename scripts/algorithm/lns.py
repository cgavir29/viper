import random as rnd
from . import solucion as sol
from . import clase as cl
from . import horario as hr
from . import profesor as pr
from copy import deepcopy

def sort_keys(clases_index):
    pass


def get_clases_index(esc):
    clases_index = []
    for iden in esc.get_clases().keys():
        clases_index.append(iden)

    clases_index.sort(key=lambda x: len(esc.get_clase(x).get_cands()))
    print(clases_index)

    return clases_index


# fixes holes with whatever it finds FROM the class candidates
def rnd_gene_repair(esc, clase, sol):
    
    # clase.sort_cands()

    total_profs = len(clase.get_cands());
    if total_profs == 0:
        return sol.get_prof("nocand")        
    
    cand_id = rnd.choice(clase.candidates)
    cand = sol.get_prof(cand_id)
    # print("im fucking hallucinating", cand)
    if cand == None:
        cand = esc.get_prof(cand_id)
        
    used_profs = set()
    
    # print("HORARIO CLASE\n", clase.get_horario(), "---------------")
    while (not cand.is_avail(clase, esc)) or ((cand.get_id() in used_profs)):
        # print(cand, "\n", cand.get_horario())
        # if not cand.is_avail(clase.horario):
        #     print("not available")
        # elif cand.get_id() in used_profs:
        #     print("in used profs")
            
        if len(used_profs) >= total_profs:
            # print("HOLE")
            return sol.get_prof("nocand")
        
        used_profs.add(cand_id)
        cand_id = rnd.choice(clase.candidates)
        cand = sol.get_prof(cand_id)
        if cand == None:
            cand = esc.get_prof(cand_id)
            
     
        
    # print(cand, len(used_profs), clase)
    # print("im fucking hallucinating again", cand)
    # print(cand)
    return cand


# gives us a random solution, real good
def gen_rndsol(esc, clases_index=None):
    if not clases_index:
        clases_index = esc.get_clases().keys() 

    solb = sol.Solucion()
    for cla_id in clases_index:
        cla = esc.get_clase(cla_id)
        # cla.sort_cands(esc)   #already sorted in simdata     
        prof = rnd_gene_repair(esc, cla, solb)
        # print("conf", prof)
        # print(prof.get_horario())
        if solb.get_prof(prof.get_id()) == None:
            # solb.profs[prof.get_id()] = [copy_prof(prof), 0]
            solb.add_prof(prof)
        solb.set_clprof(cla, prof.get_id())
        # print(prof.get_horario())

        
    return solb


def gene_repair_cands(esc, clase, sol): 
    total_profs = len(clase.get_cands())

    if total_profs == 0:
        return sol.get_prof("nocand")

    cand_id = clase.get_cands()[0]
    cand = sol.get_prof(cand_id)
    
    if cand == None:
        cand = esc.get_prof(cand_id)

    index = 0
    
    while not cand.is_avail(clase, esc):
        if index >= total_profs:
            return sol.get_prof("nocand")
        
        cand_id = clase.get_cands()[index]
        cand = sol.get_prof(cand_id)
        if cand == None:
            cand = esc.get_prof(cand_id)
            
        index += 1
        

    return cand


# uses gene_repair_cands to create a solution
def greedy_sol(esc, clases_index):
    solb = sol.Solucion()
    for claid in clases_index:
        cla = esc.get_clase(claid)
        cla.sort_cands(esc)        
        prof = gene_repair_cands(esc, cla, solb)

        if solb.get_prof(prof.get_id()) == None:
            # solb.profs[prof.get_id()] = [copy_prof(prof), 0]
            solb.add_prof(prof)

        solb.set_clprof(cla, prof.get_id())
    return solb


def destroy_by_classnum(sol, amount_des, esc):
    profs_num_clase = list(sol.get_profs().keys())  # profs id's
    if len(profs_num_clase) < amount_des:
        amount_des = int(len(profs_num_clase)/3)
    # print(sol_asigs)
    # sort prof's id's  by the number of classes
    profs_num_clase.sort(key=lambda x: sol.get_num_clases(x))
    poor_sods = set()
    for i in range(amount_des):
        poor_sods.add(profs_num_clase[i])        
    
    for clase_id in sol.get_clprofs().keys():
        assig = sol.get_clprof(clase_id)[0]
        clase = esc.get_clase(clase_id)
        if assig in poor_sods and len(clase.get_cands())>1:
            sol.add_hole(clase)
        



def destroy_rand_cl(sol, rnd_des, esc):
    percent = rnd_des/len(esc.get_clases())*10
    for clase in esc.get_clases().values():
        roll = rnd.random() * 10
        if (roll) <= percent:
            sol.add_hole(clase)
    
    
def destroy_rand_cl_ex(sol, rnd_des, esc):
    sol_asigs = list(sol.clase_prof.keys())  # class id's
    used = set()
    if len(sol_asigs) < rnd_des:
        rnd_des = int(len(sol_asigs)/3)
    
    while len(used) <= rnd_des:
        target_clase_id = rnd.choice(sol_asigs)
        target_clase = esc.get_clase(target_clase_id)
        if target_clase_id not in used and not sol.has_hole(target_clase):
            if len(target_clase.get_cands()>1):
                sol.add_hole(target_clase)
            used.add(target_clase_id)

        


def repair_greedy(sol, esc):
    piece_of_shit_me = deepcopy(sol.get_holes())

    for hole in piece_of_shit_me:
        clase_ref = esc.get_clase(hole)
        prof = gene_repair_cands(esc, clase_ref, sol);
        if sol.get_prof(prof.get_id()) == None:
            sol.add_prof(prof)
        sol.set_clprof(clase_ref, prof.get_id())        
    
  




def would_be_underass(sol, esc, claseid, prof_min):
    employed_h = lambda t: t.get_horario().get_total_h()
    prof_id = sol.get_clprof(claseid)[0]
    prof = sol.get_prof(prof_id)
    clase = esc.get_clase(claseid)

    if employed_h(prof) - employed_h(clase) < prof_min:
        return True
    return False


        
def balance_class_assigs(sol, esc, clases_index):

    #whos aight and whos not------------------------------------
    employed_h = lambda t: t.get_horario().get_total_h()
    under_ass_teachers = {}

    # print(sol.get_profs())
    for (teacher_tup) in sol.get_profs().values():
        teacher = teacher_tup[0]

        
        min_h = 20
        if teacher.get_mhor() < 20:
            min_h = teacher.get_mhor()

            
        if employed_h(teacher) > 0 and employed_h(teacher) < int(min_h * 0.8):
            under_ass_teachers[teacher.get_id()] = set()
    #-----------------------------------------------------------  

    
    #get the classes for each one-------------------------------
    for clase in esc.get_clases().values():
        for cand in clase.get_cands():
            if cand in under_ass_teachers:
                under_ass_teachers[cand].add(clase.get_id())
    #-----------------------------------------------------------

    
    #sort em by those who are closer to being fine ------------
    under_ass_ids = list(under_ass_teachers.keys())
    under_ass_ids.sort(key = lambda t: employed_h(sol.get_prof(t)),
                       reverse = True)
    #-----------------------------------------------------------
    
    for poor_sod_id in under_ass_ids:
        poor_sod = sol.get_prof(poor_sod_id)#poor sod object
        min_h = 20
        
        if teacher.get_mhor() < 20:
            min_h = teacher.get_mhor() #adjust the minimum hours
            
        for pot_clase_id in under_ass_teachers[poor_sod_id]: #for each class he can teach
            if not would_be_underass(sol, esc,  pot_clase_id, min_h): #if the current prof wouldnt become a poor sod
               if employed_h(poor_sod) >= int(min_h): #if the poor sod is fool break it
                   break

               pot_clase = esc.get_clase(pot_clase_id) #get the class
               if poor_sod.is_avail(pot_clase, esc): #check if the poor sod can teach
                   sol.set_clprof(pot_clase, poor_sod_id) #assign him
                   
    sol.print_info()
               

def do_lns(sol, esc, silly_teachers, shook_classes, clases_index = None):
    if not clases_index:
        clases_index = get_clases_index(esc)
    destroy_by_classnum(sol, silly_teachers, esc)
    destroy_rand_cl(sol, shook_classes, esc)
    repair_greedy(sol, esc)













    
    


    

    
