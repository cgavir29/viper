import solucion as sol, clase as cl, horario as hr, profesor as pr, simdata as sm, random as rnd
from copy import deepcopy

def sort_keys(clases_index):
    pass


def get_clases_index(esc):
    clases_index = []
    for iden in esc.get_clases().keys():
        clases_index.append(iden)

    clases_index.sort(key=lambda x: len(esc.get_clase(x).get_cands()), reverse=True)

    return clases_index


# fixes holes with whatever it finds FROM the class candidates
def rnd_gene_repair(esc, clase, sol):
    
    # clase.sort_cands()
    
    cand_id = rnd.choice(clase.candidates)
    cand = sol.get_prof(cand_id)
    # print("im fucking hallucinating", cand)
    if cand == None:
        cand = esc.get_prof(cand_id)
        
    total_profs = len(clase.get_cands());
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
def gen_rndsol(esc):
    solb = sol.Solucion()
    for cla in esc.get_clases().values():
        # cla.sort_cands(esc)   #already sorted in simdata     
        prof = rnd_gene_repair(esc, cla, solb)
        # print("conf", prof)
        # print(prof.get_horario())
        if solb.get_prof(prof.iden) == None:
            # solb.profs[prof.iden] = [copy_prof(prof), 0]
            solb.add_prof(prof)
        solb.set_clprof(cla, prof.iden)
        # print(prof.get_horario())

        
    return solb


# tries to fit every hole with the best possible candidates in the class
def gene_repair_cands(esc, clase, sol):    
    cand_id = clase.get_cands()[0]
    cand = sol.get_prof(cand_id)
    
    if cand == None:
        cand = esc.get_prof(cand_id)

    total_profs = len(clase.get_cands())
    index = 0
    
    while not cand.is_avail(clase, esc):
        if index >= total_profs:
            return sol.get_prof("nocand")
        
        cand_id = clase.get_cands()[index]
        cand = sol.get_prof(cand_id)
        if cand == None:
            cand = esc.get_prof(cand_id)
            
        index+=1
        

    return cand


# uses gene_repair_cands to create a solution
def greedy_sol(esc, clases_index):
    solb = sol.Solucion()
    for claid in clases_index:
        cla = esc.get_clase(claid)
        cla.sort_cands(esc)        
        prof = gene_repair_cands(esc, cla, solb)

        if solb.get_prof(prof.iden) == None:
            # solb.profs[prof.iden] = [copy_prof(prof), 0]
            solb.add_prof(prof)

        solb.set_clprof(cla, prof.iden)
    return solb


def destroy_by_classnum(sol, amount_des, esc):
    profs_num_clase = list(sol.get_profs().keys())  # profs id's
    # print(sol_asigs)
    # sort prof's id's  by the number of classes
    profs_num_clase.sort(key=lambda x: sol.get_num_clases(x))
    poor_sods = set()
    for i in range(amount_des):
        poor_sods.add(profs_num_clase[i])        
    
    for clase_id in sol.get_clprofs().keys():
        assig = sol.get_clprof(clase_id)[0]
        clase = esc.get_clase(clase_id)
        if assig in poor_sods:
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

    
    while len(used) <= rnd_des:
        target_clase_id = rnd.choice(sol_asigs)
        target_clase = esc.get_clase(target_clase_id)
        if target_clase_id not in used and not sol.has_hole(target_clase):
            used.add(target_clase_id)
            sol.add_hole(target_clase)

        


def repair_greedy(sol, esc):
    piece_of_shit_me = deepcopy(sol.get_holes())

    for hole in piece_of_shit_me:
        clase_ref = esc.get_clase(hole)
        prof = gene_repair_cands(esc, clase_ref, sol);
        if sol.get_prof(prof.iden) == None:
            sol.add_prof(prof)
        sol.set_clprof(clase_ref, prof.iden)        
    
  

def balance_class_assigs(sol, esc):
    employed_h = lambda t: t.get_horario().get_total_h()
    aight_teachers = set()
    for teacher in sol.get_profs():
        if employed_h > 22: 
            aight_teachers.add(teacher)

    for (claid, (profid,_)) in sol.get_clprofs().items():
        prof = sol.get_prof(profid)
        if prof in aight_teachers:
            print("finish balance_class_asigs")
        
        
    
    pass
    
    
    


def do_lns(sol, esc, silly_teachers, shook_classes):
    clases_index = get_clases_index(esc)
    destroy_by_classnum(sol, silly_teachers, esc)
    destroy_rand_cl(sol, shook_classes, esc)
    repair_greedy(sol, esc)













    
    


    
