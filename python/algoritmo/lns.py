import solucion as sol, clase as cl, horario as hr, profesor as pr, simdata as sm, random as rnd
from helper import copy_prof, merge_hashes


# some_cursos = sm.gen_courses()
# some_clases = sm.gen_clases(some_cursos)
# some_profs = sm.gen_rand_profs(250, some_clases, 0.7, 1, True)
# some_clases_index = list(some_clases.keys())
# # some_clases_index.sort(key=lambda a: len(some_clases[a].candidates))
# print("we're talking", len(some_profs), "profs")
# print("and", len(some_clases), "clases")


def sort_keys(clases_index):
    pass


# This function helps us count holerinos in a solution
def count_holes(sol):
    sol_asigs = list(sol.clase_prof.keys())  # class id's
    num = 0
    for i in sol_asigs:
        if sol.get_clprof(i) == None:
            num += 1
    print(num, "empty assignments")


# fixes holes with whatever it finds FROM the class candidates
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


# gives us a random solution, real good
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


# tries to fit every hole with the best possible candidates in the class
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
        prof = sol.get_prof(candid)
        if prof == None:
            prof = profs.get(candid)
        # else:
        #     print(prof.horario.count_avail())

        index += 1
    # print(prof.iden, "index", index, "\n")
    # print(clase.candidates[0:3])

    return prof


# uses gene_repair_cands to create a solution
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
    des_cl = {}
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
                des_cl[j] = 1
    return des_cl


def destroy_rand_cl(sol, rnd_des, clases):
    sol_asigs = list(sol.clase_prof.keys())  # class id's
    des_cl = {}
    for _ in range(rnd_des):
        # print(sol.active_profs)
        target_class = rnd.choice(sol_asigs)
        asig = sol.get_clprof(target_class)
        while asig == None:  # improve this by changing to a has later
            target_class = rnd.choice(sol_asigs)
            asig = sol.get_clprof(target_class)

        des_cl[target_class] = 1
        clase = clases.get(target_class)
        sol.del_clprof(clase)
        asig = sol.get_clprof(target_class)
        if asig != None:
            print(index, i, asig)
            raise NameError("something is not right in destroy_rand_cl 1")

    return des_cl


def repair_simple_greedy(sol, clases, profs, holes):
    index = 0
    seen = {}
    holes = list(holes.keys())
    # THIS WHILE LOOP IS EXPERIMENTAL
    # i think that destroy by classnum
    # returns a list that still holds a certain order
    # i want to see what happens if i get rid of that order
    
    while len(seen) < len(holes):
        hole = rnd.choice(holes)
        while seen.get(hole)==1:
            hole = rnd.choice(holes)
        seen[hole] = 1
        asig = sol.get_clprof(hole)
        if asig != None:
            raise NameError("something is not right in destroy_rand_cl")
        index += 1
        clase = clases.get(hole)
        prof = gene_repair_cands(profs, clase, sol)

        # if the prof has not been added yet
        if sol.get_prof(prof.iden) == None:
            sol.add_prof(copy_prof(profs.get(prof.iden)))
        sol.set_clprof(clase, prof.iden)


"""    
    for i in holes:
        asig = sol.get_clprof(i)
        # print(i)
        if asig != None:
            print(index, i, asig)
            raise NameError("something is not right in destroy_rand_cl")
        index += 1
        clase = clases.get(i)
        prof = gene_repair_cands(profs, clase, sol)
        # prof = gene_repair_cands(profs, clase, sol)

        #if the prof has not been added yet
        if not sol.get_prof(prof.iden):
            sol.add_prof(copy_prof(profs.get(prof.iden)))
        sol.set_clprof(clase, prof.iden)
"""


def balance_class_assigs(sol, clases, profs, holes):
    # run destroy_rand_cl before this
    pass


def do_lns(sol, profs, clases_index, clases, silly_teachers=0, shook_classes=0, extra_holes = {}):

    sort_keys(clases_index)

    silly_ones = {}
    if silly_teachers < 0:
            silly_teachers = int(input("how many underassigned teachers should be removed? "))
            
    if silly_teachers:     
        silly_ones = destroy_by_classnum(sol, silly_teachers, clases)
        
    if shook_classes < 0:
        shook_classes = int(input("how many classes shall be  s h o o k? "))
    shook_ones = {}
    if shook_classes:
        shook_ones = destroy_rand_cl(sol, shook_classes, clases)

    # save the destroyed  classes randomly
    stupid_hash= merge_hashes(shook_ones, silly_ones)
    
    repair_simple_greedy(sol, clases, profs,merge_hashes(stupid_hash, extra_holes))
    
















    
# greed = greedy_sol(some_profs, some_clases_index, some_clases)
# # greed = gen_rndsol(some_profs, some_clases_index, some_clases)
# print("greed scored", greed.score, "with", greed.active_profs, "profs")
# count_holes(greed)
# do_lns(greed, some_profs, some_clases_index, some_clases, 30, 30)


# #t h i s     d o e s n t     c o n s i d e r    c e r t s
# #this function just takes the best available teachers from the class
# #doesnt really work too good. will comment
# eventually, if they allow for teachers who do not have the certs to
# teach a class, it becomes useful
# def gene_repair_clprofs(clase, sol):
#     profs = [x[0] for x in list(sol.profs.values())]
#     profs.sort(key=lambda x: clase.eval_prof(x), reverse=True)
#     prof = profs[0]  # best solution
#     index = 0
#     # print(len(clase.candidates))

#     while not prof.is_avail(clase.horario):
#         prof = profs[index]
#         # print("cand prof", prof.iden)
#         index += 1

# return prof
