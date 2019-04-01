import solucion as sol, clase as cl, horario as hr, profesor as pr, simdata as sm, random as rnd
from helper import copy_prof


some_cursos = sm.gen_courses()
some_clases = sm.gen_clases(some_cursos)
some_profs = sm.gen_rand_profs(250, some_clases, 0.7, 1, True)
some_clases_index = list(some_clases.keys())
some_clases_index.sort(key=lambda a: len(some_clases[a].candidates))
print("we're talking", len(some_profs), "profs")
print("and", len(some_clases), "clases")


def count_holes(sol):
    sol_asigs = list(sol.clase_prof.keys())  # class id's
    num = 0
    for i in sol_asigs:
        if sol.get_clprof(i) == None:
            num += 1
    print(num, "empty assignments")


def rnd_gene_repair(profs, clase, sol):
    candid = clase.candidates[0][0]  # best solution
    prof = sol.get_prof(candid)
    if prof == None:
        prof = profs[candid]

    while not prof.is_avail(clase.horario):
        candid = rnd.choice(clase.candidates)[0]
        prof = sol.get_prof(candid)
        if prof == None:
            prof = profs[candid]
    # if you move to rust, you can make this a reference
    return prof


def gen_rndsol(profs, clases_index, clases):
    solb = sol.Solucion()
    for claid in clases_index:
        cla = clases.get(claid)
        prof = rnd_gene_repair(profs, cla, solb)
        
        if solb.get_prof(prof.iden) == None:
            # solb.profs[prof.iden] = [copy_prof(prof), 0]
            solb.add_prof(copy_prof(prof))

        solb.set_clprof(cla, prof.iden)
    return solb


def gene_repair_cands(profs, clase, sol):
    # print(clase.horario)
    candid = clase.candidates[0][0]  # best solution
    prof = sol.get_prof(candid)
    
    if prof == None:
        prof = profs.get(candid)

    index = 1
    # print(len(clase.candidates))
    while not prof.is_avail(clase.horario):
        # print(pair, "i")
        # print(prof.is_avail(clase.horario), index)
        candid = clase.candidates[index][0]
        prof = sol.get_prof(candid);
        if prof == None:
            prof = profs.get(candid)
        # else:
        #     print(prof.horario.count_avail())
            
        index += 1
    # print(prof.iden, "index", index, "\n")
    # print(clase.candidates[0:3])
    
    return prof


def gene_repair_clprofs(clase, sol):
    profs = [x[0] for x in list(sol.profs.values())]
    profs.sort(key=lambda x: clase.eval_prof(x), reverse=True)
    prof = profs[0]  # best solution
    index = 0
    # print(len(clase.candidates))

    while not prof.is_avail(clase.horario):
        prof = profs[index]
        # print("cand prof", prof.iden)
        index += 1
    
    return prof


def greedy_sol(profs, clases_index, clases):
    solb = sol.Solucion()
    for claid in clases_index:
        cla = clases.get(claid)
        prof = gene_repair_cands(profs, cla, solb)

        if solb.get_prof(prof.iden) == None:
            # solb.profs[prof.iden] = [copy_prof(prof), 0]
            solb.add_prof(copy_prof(prof))
            
        solb.set_clprof(cla, prof.iden)
    return solb


def destroy_by_classnum(sol, amount_des, clases):
    profs_num_class = list(sol.profs.keys())  # profs id's
    sol_asigs = list(sol.clase_prof.keys())  # class id's
    # print(sol_asigs)
    # sort prof's id's  by the number of classes
    profs_num_class.sort(key=lambda x: sol.profs.get(x)[1])

    # delete all assignments of that profesor
    for i in range(amount_des):
        old_prof = profs_num_class[i]
        # print(type(old_prof))
        # print(sol.profs.get(old_prof)[1])
        for j in sol_asigs:
            asig = sol.clase_prof.get(j)  # the class assignment
            # if this class is assigned to the prof we're looking for
            # delete the assignment
            # it might be none if it was unasigned previously
            # when removing another teacher
            if asig != None and asig[0] == old_prof:
                # making it None should  NOT remove the key,
                # already testd
                # print("old prof", old_prof)

                clase = clases.get(j)
                # print(j, old_prof, list(clase.curso.reqr.keys()))
                # print(len(clase.candidates))
                # vals = [x[1] for x in clase.candidates]
                # print(sum(vals)/len(vals))
                
                sol.del_clprof(clase)


def destroy_rand_cl(sol, rnd_des, clases):
    sol_asigs = list(sol.clase_prof.keys())  # class id's
    for _ in range(rnd_des):
        # print(sol.active_profs)
        target_class = rnd.choice(sol_asigs)
        clase = clases.get(target_class)
        sol.del_clprof(clase)


def repair_simple_greedy(sol, clases, profs):
    sol_asigs = list(sol.clase_prof.keys())  # class id's
    for i in sol_asigs:
        asig = sol.clase_prof.get(i)
        if asig == None:
            clase = clases.get(i)
            prof = gene_repair_clprofs(clase, sol)
            # prof = gene_repair_cands(profs, clase, sol)
            sol.set_clprof(clase, prof.iden)


greed = greedy_sol(some_profs, some_clases_index, some_clases)
print("greed scored", greed.score, "with", greed.active_profs, "profs")
count_holes(greed)


destroy_by_classnum(greed, 50, some_clases)
print("after first destruction:", greed.score, "with", greed.active_profs, "profs")
count_holes(greed)

destroy_rand_cl(greed, 100, some_clases)
print("after rand destruction:", greed.score, "with", greed.active_profs, "profs")
count_holes(greed)

repair_simple_greedy(greed, some_clases, some_profs)
print("after simple repair:", greed.score, "with", greed.active_profs, "profs")
count_holes(greed)
