import random as rnd, solucion as sol, copy, time as tm, simdata as sm, profesor as pr, horario as hr


some_cursos = sm.gen_courses()
some_clases = sm.gen_clases(some_cursos)
some_profs = sm.gen_rand_profs(400, some_clases)
# list of keys in the dictionary in order to
# sort them so that classes with less candidates get assgined
# first
some_clases_index = list(some_clases.keys())
some_clases_index.sort(key=lambda a: len(some_clases[a].candidates))
print("we're talking", len(some_profs), "profs")
print("and", len(some_clases), "clases")


# test_cursos = sm.gen_courses_tiny()
# test_clases = sm.gen_clases_tiny(test_cursos)
# test_profs = sm.gen_rand_profs(100, test_clases)
# test_clases_index = list(test_clases.keys())
# test_clases_index.sort(key=lambda a: len(test_clases[a].candidates))
# print("we're talking", len(test_profs), "profs")
# print("and", len(test_clases), "clases")






# utility functions ----------------------------------
def chk_sch(prof_col):
    prev = rnd.choice(list(prof_col.items()))[1]
    prev = prev.horario.count_avail()
    for p2 in prof_col:
        p = prof_col.get(p2)
        curr = p.horario.count_avail()
        if curr != prev:
            raise NameError("shit nigga")
        prev = curr
    print(prev)


def copy_prof(prof):
    sch = hr.Horario()
    for dia in prof.horario.diario:
        for hora in prof.horario.diario.get(dia):
            sch.diario[dia][hora] = prof.horario.get_horario(dia, hora)

    return pr.Profesor(prof.iden, sch, prof.score)


def find_champ(popul):
    champ = max(popul, key = lambda a : a.score)
    print("CHAMP IS", champ.score)
    
# utility functions ----------------------------------


def gen_rndsol(profs, clases_index, clases):
    sola = sol.Solucion()
    for claid in clases_index:
        # get the class
        cla = clases.get(claid)

        # get some profid that can teach the class
        profid = rnd.choice(cla.candidates)[0]

        # get the actual object from solution
        prof = sola.get_prof(profid)

        # if the teacher is not in the sol
        # yet get the default
        if prof == None:
            prof = profs.get(profid)

        # print(cla.horario)
        while not prof.is_avail(cla.horario):
            profid = rnd.choice(cla.candidates)[0]
            prof = sola.get_prof(profid)
            # if the teacher is not in the sol
            # yet get the default
            if prof == None:
                prof = profs.get(profid)

        if sola.get_prof(profid) == None:
            sola.profs[profid] = copy_prof(prof)

        # chk_sch(profs)
        sola.set_clprof(cla, prof.iden)

    return sola


def rnd_popul(size, profs, clases_index, clases):
    ini = tm.time()
    population = []
    for i in range(size):
        ini_ind = tm.time()
        population.append(gen_rndsol(profs, clases_index, clases))
        print("solution", i, "done in", tm.time() - ini_ind, end="\r")
        # chk_sch()
    return population


# RETURNS **A REFERENCE** TO A TEACHER THAT CAN TEACH A GIVEN CLASS
# CONSIDERING HSI SHCEDULE IN A SOLUTION
def gene_repair(profs, clase, sol):
    candid = clase.candidates[0][0]  # best solution
    prof = sol.get_prof(candid)

    # the best profesor has not yet been included
    # in sol, so take the default, no need to copy
    # since i only need the schedule

    # SHEDULES ARE ONLY FULL AVAILABLE IN THE TEST RUN
    if prof == None:
        prof = profs[candid]
        # print("gene repair, not loop, chckavail", prof.horario.count_avail())

    index = 1
    while not prof.is_avail(clase.horario):
        candid = clase.candidates[index][0]
        prof = sol.get_prof(candid)

        # if the candid is not included yet
        # add the default, no need to copy in theory
        if prof == None:
            prof = profs[candid]
            # print("gene repair, loop chckavail", prof.horario.count_avail())

        index += 1
    # print(prof)
    return prof





# RETURNS **A REFERENCE** TO A TEACHER THAT CAN TEACH A GIVEN CLASS
# CONSIDERING HSI SHCEDULE IN A SOLUTION, but generated randomly
def rnd_gene_repair(profs, clase, sol):
    candid = clase.candidates[0][0]  # best solution
    prof = sol.get_prof(candid)

    # the best profesor has not yet been included
    # in sol, so take the default, no need to copy
    # since i only need the schedule

    # SHEDULES ARE ONLY FULL AVAILABLE IN THE TEST RUN
    if prof == None:
        prof = profs[candid]
        # print("gene repair, not loop, chckavail", prof.horario.count_avail())

    while not prof.is_avail(clase.horario):
        candid = rnd.choice(clase.candidates)[0]
        prof = sol.get_prof(candid)
        # if the candid is not included yet
        # add the default, no need to copy in theory
        if prof == None:
            prof = profs[candid]
            # print("gene repair, loop chckavail", prof.horario.count_avail())

    # print(prof)
    return prof




#TODO: 
def greedy_sol(profs, clases_index, clases):
    pass
    





# clases here should be clases_index
def cross_over(profs, clases_index, clases, parent1, parent2, rate):
    roll = rnd.random()
    child1 = sol.Solucion()
    child2 = sol.Solucion()
    # chk_sch(profs)
    if roll <= rate:
        co_point = rnd.randint(1, len(parent1.clase_prof) - 2)
        # print("len of sol", len(parent1.clase_prof))
        index = 0   
        for claseid in clases_index:
            clase = clases.get(claseid)
            
            info1 = parent1.get_clprof(clase.iden)
            #if you take the teacher from parent 1
            #he will already have his schedule taken
            #we want the defult
            prof1 = profs.get(info1[0])
            
            info2 = parent2.get_clprof(clase.iden)
            prof2 = profs.get(info2[0])

            # if index == co_point:
            #     print("cross over class", clase)

            
            if index <= co_point:
                index+=1
                # check my hypothesis that it doesnt mtter
                # print(prof1.horario.count_avail()

                # if the profesor is not in the child solution yet
                # include copy of the default
                # do not include a copy of prof 1 because it already
                # has its whole shcedule assigned
                if child1.get_prof(prof1.iden) == None:
                    child1.profs[prof1.iden] = copy_prof(profs[prof1.iden])
                    
                if not child1.get_prof(prof1.iden).is_avail(clase.horario):
                    raise NameError("ooga booga you were wrong nigga")

                child1.set_clprof(clase, prof1.iden)


                # if the profesor is not in the child solution yet
                # include copy of the default
                # do not include a copy of prof 2 because it already
                # has its whole shcedule assigned
                if child2.get_prof(prof2.iden) == None:
                    child2.profs[prof2.iden] = copy_prof(profs[prof2.iden])

                if not child2.get_prof(prof2.iden).is_avail(clase.horario):
                    raise NameError("ooga booga you were wrong nigga")

                    
                child2.set_clprof(clase, prof2.iden)


            else:
                index+=1
                # here we need to check if it can be done
                # use the profs in child classes not parents
                # (it should be the same at first but as you add
                # more)
                # first i will try to insert a prof from parent2 into
                # the class in child1
                p2c1prof = child1.get_prof(prof2.iden)

                # if the teacher has not yet been included,
                # get the default, no need to copy here
                if p2c1prof == None:
                    p2c1prof = profs[prof2.iden]

                # get another one in case he's not availale
                if not p2c1prof.is_avail(clase.horario):
                    # print(clase, "child1", p2c1prof)
                    p2c1prof = gene_repair(profs, clase, child1)

                # by this point p2c1prof should be able to teach

                # if the sol didnt have him, include him
                if child1.get_prof(p2c1prof.iden) == None:
                    child1.profs[p2c1prof.iden] = copy_prof(p2c1prof)

                child1.set_clprof(clase, p2c1prof.iden)

                # the same for child2
                p1c2prof = child2.get_prof(prof1.iden)

                if p1c2prof == None:
                    p1c2prof = profs[prof1.iden]

                if not p1c2prof.is_avail(clase.horario):
                    # print(clase, "child2", p1c2prof)                    
                    p1c2prof = gene_repair(profs, clase, child2)

                if child2.get_prof(p1c2prof.iden) == None:
                    child2.profs[p1c2prof.iden] = copy_prof(p1c2prof)

                child2.set_clprof(clase, p1c2prof.iden)
        
                
        return (child1, child2)
    
    else:
        return (parent1, parent2)

    



def mutation(profs, clases_index, clases, subject1, subject2, rate):
    roll = rnd.random()

    for claseid in clases_index:
        clase = clases.get(claseid)
        if roll <= rate:
            prof = rnd_gene_repair(profs, clase, subject1)
            if subject1.profs.get(prof.iden) == None:
                subject1.profs[prof.iden] = copy_prof(prof)
            
            subject1.set_clprof(clase, prof.iden)
        roll = rnd.random()
        
        if roll <= rate:
            prof = rnd_gene_repair(profs, clase, subject2)
            if subject2.profs.get(prof.iden) == None:
                subject2.profs[prof.iden] = copy_prof(prof)
                
            subject2.set_clprof(clase,prof.iden)

        roll = rnd.random()



def roulette(p_size, fit_hash, t_fitness):
    roll = rnd.uniform(t_fitness/5, t_fitness)
    roll = rnd.uniform(0, t_fitness)    
    p_fitness = 0
    fitness = 0 
    
    for i in range(p_size):
        fitness = fit_hash[i][0]
        p_fitness += fitness
        if p_fitness >= roll:
            return fit_hash[i][1]
        
    raise NameError("roulette isnt working what")

        
def do_gen(profs, clases_index, clases, p_size, co_rate, mu_rate, gens):
    population = rnd_popul(p_size, profs, clases_index, clases)
    find_champ(population)

    gen_count = 0
    fit_hash = []

    succs = []
    start = tm.time()

    while gen_count < gens:
        start2 = tm.time()
        t_fitness = 0
        fitness = 0

        for i in range(p_size):
            fitness = population[i].score
            fit_hash.append((fitness, i))
            t_fitness += fitness

        print("\nthis gen", gen_count, "has", t_fitness/p_size, " avg fitnerinos")

        #doesnt seem to make a huge difference in result
        fit_hash.sort(key = lambda tup : tup[0])

        avg_parent_score = 0
        
        while len(succs) < p_size:
            index1 = roulette(p_size, fit_hash, t_fitness)
            index2 = roulette(p_size, fit_hash, t_fitness)

            parent1 = population[index1]
            parent2 = population[index2]

            avg_parent_score += parent1.score + parent2.score


            children = cross_over(profs, clases_index, clases,  parent1, parent2, co_rate)

            mutation(profs, clases_index, clases, parent1, parent2, mu_rate)
            succs.append(children[0])
            succs.append(children[1])

        population = succs
        succs = []
        fit_hash.clear()

        this_time = tm.time() - start2
        find_champ(population)
        print("generation", gen_count, "took:", this_time)
        gen_count+=1

        print("\nMEASUREMENTS_____________________")
        print("avg parent score", avg_parent_score/p_size)
        print("END MEASUREMENTS_________________")
        
    print("finished genetic recombination!")
    t_time = tm.time()- start
    find_champ(population)
    print("found in", t_time, "avg gen took", t_time/gens)
        

    

    


do_gen(some_profs, some_clases_index, some_clases, 1200, 0.7, 0.001, 100)


