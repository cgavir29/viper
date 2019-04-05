import random as rnd, solucion as sol, copy, time as tm, simdata as sm, profesor as pr, horario as hr
from helper import copy_prof
import lns

some_cursos = sm.gen_courses()
some_clases = sm.gen_clases_full(some_cursos)
some_profs = sm.gen_rand_profs(400, some_clases, 0.75, 1, True)
some_clases_index = list(some_clases.keys())
# some_clases_index.sort(key=lambda a: len(some_clases[a].candidates))
print("we're talking", len(some_profs), "profs")
print("and", len(some_clases), "clases")


# fstcl = some_clases[some_clases_index[0]]
# sndcl = some_clases[some_clases_index[-1]]
# if len(fstcl.candidates) ==  len(sndcl.candidates):
#     print(len(fstcl.candidates), len(sndcl.candidates))
#     raise NameError("The sort is acting weird")


def lns_test():
      print("\nlns greedy-----------------------------------------------")
      greed = lns.greedy_sol(some_profs, some_clases_index, some_clases)
      print("greed scored", greed.score, "with", greed.active_profs, "profs")

      print("starting lns loop")
      greed = lns.gen_rndsol(some_profs, some_clases_index, some_clases)
      for i in range(600):
          # lns.count_holes(greed)
          lns.do_lns(greed, some_profs, some_clases_index, some_clases, 30, 30)

      print("greed scored", greed.score, "with", greed.active_profs, "profs")    
      print("lns greedy-----------------------------------------------\n")

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


def find_champ(popul):
    champ = max(popul, key=lambda a: a.score)
    print("CHAMP IS", champ.score, "with", champ.active_profs, "                  ")


# utility functions ----------------------------------


def gen_rndsol(profs, clases_index, clases):
    sola = sol.Solucion()
    for claid in clases_index:
        cla = clases.get(claid)
        profid = rnd.choice(cla.candidates)[0]
        prof = sola.get_prof(profid)

        if prof == None:
            prof = profs.get(profid)

        while not prof.is_avail(cla.horario):
            profid = rnd.choice(cla.candidates)[0]
            prof = sola.get_prof(profid)
            if prof == None:
                prof = profs.get(profid)

        if sola.get_prof(profid) == None:
            # sola.profs[profid] = [copy_prof(prof), 0]
            sola.add_prof(copy_prof(prof))

        sola.set_clprof(cla, prof.iden)

    return sola


def rnd_popul(size, profs, clases_index, clases):
    ini = tm.time()
    population = []
    for i in range(size):
        ini_ind = tm.time()
        population.append(gen_rndsol(profs, clases_index, clases))
        print("solution", i, "done in", tm.time() - ini_ind, end="\r")
    return population


# RETURNS **A REFERENCE** TO A TEACHER THAT CAN TEACH A GIVEN CLASS
# CONSIDERING HSI SHCEDULE IN A SOLUTION
def gene_repair(profs, clase, sol):
    candid = clase.candidates[0][0]  # best solution
    prof = sol.get_prof(candid)

    if prof == None:
        prof = profs[candid]

    index = 1
    while not prof.is_avail(clase.horario):
        candid = clase.candidates[index][0]
        prof = sol.get_prof(candid)

        if prof == None:
            prof = profs[candid]

        index += 1
    return prof


# RETURNS **A REFERENCE** TO A TEACHER THAT CAN TEACH A GIVEN CLASS
# CONSIDERING HSI SHCEDULE IN A SOLUTION, but generated randomly
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


# TODO:
def greedy_sol(profs, clases_index, clases):
    pass


def cross_over(profs, clases_index, clases, parent1, parent2, rate):
    roll = rnd.random()
    child1 = sol.Solucion()
    child2 = sol.Solucion()

    if roll <= rate:
        co_point = rnd.randint(1, len(parent1.clase_prof) - 2)
        index = 0
        for claseid in clases_index:
            clase = clases.get(claseid)

            info1 = parent1.get_clprof(clase.iden)
            prof1 = profs.get(info1[0])

            info2 = parent2.get_clprof(clase.iden)
            prof2 = profs.get(info2[0])

            if index <= co_point:
                index += 1
                if child1.get_prof(prof1.iden) == None:
                    generic_pr = copy_prof(profs[prof1.iden])
                    # child1.profs[prof1.iden] = [copy_prof(profs[prof1.iden]), 0]
                    child1.add_prof(generic_pr)

                if not child1.get_prof(prof1.iden).is_avail(clase.horario):
                    raise NameError("ooga booga you were wrong nigga")

                child1.set_clprof(clase, prof1.iden)

                if child2.get_prof(prof2.iden) == None:
                    generic_pr = copy_prof(profs[prof2.iden])
                    # child2.profs[prof2.iden] = [copy_prof(profs[prof2.iden]),0]
                    child2.add_prof(generic_pr)

                if not child2.get_prof(prof2.iden).is_avail(clase.horario):
                    raise NameError("ooga booga you were wrong nigga")

                child2.set_clprof(clase, prof2.iden)

            else:
                index += 1
                p2c1prof = child1.get_prof(prof2.iden)
                if p2c1prof == None:
                    p2c1prof = profs[prof2.iden]

                if not p2c1prof.is_avail(clase.horario):
                    p2c1prof = gene_repair(profs, clase, child1)

                if child1.get_prof(p2c1prof.iden) == None:
                    # child1.profs[p2c1prof.iden] = [copy_prof(p2c1prof), 0]
                    child1.add_prof(copy_prof(p2c1prof))

                child1.set_clprof(clase, p2c1prof.iden)

                p1c2prof = child2.get_prof(prof1.iden)

                if p1c2prof == None:
                    p1c2prof = profs[prof1.iden]

                if not p1c2prof.is_avail(clase.horario):
                    p1c2prof = gene_repair(profs, clase, child2)

                if child2.get_prof(p1c2prof.iden) == None:
                    # child2.profs[p1c2prof.iden] = [copy_prof(p1c2prof), 0]
                    child2.add_prof(copy_prof(p1c2prof))
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
                subject1.profs[prof.iden] = [copy_prof(prof), 0]
                subject1.add_prof(copy_prof(prof))
            subject1.set_clprof(clase, prof.iden)
        roll = rnd.random()

        if roll <= rate:
            prof = rnd_gene_repair(profs, clase, subject2)
            if subject2.profs.get(prof.iden) == None:
                subject2.profs[prof.iden] = [copy_prof(prof), 0]
                subject2.add_prof(copy_prof(prof))
            subject2.set_clprof(clase, prof.iden)

        roll = rnd.random()


# 13918 13878 w sort 300 >200
# 13326 13161.51 wo sort 300 >200 seems to converge around 223


def roulette(population, split):
    #HARD SEGREGATION, SOFT SEGREGATION WOULD
    #ONLY AFFECT THE ROLL
    
    fit_hash = []
    for i in range(len(population)):
        fitness = population[i].score
        fit_hash.append((fitness, i))

    fit_hash.sort() #least fit sols first

    split_point = int(len(fit_hash)*split)

    t_fitness_inf = 0
    for i in range(split_point):
        t_fitness_inf+=fit_hash[i][0]

    t_fitness_sup = 0
    for i in range(split_point, len(fit_hash)):
        t_fitness_sup+=fit_hash[i][0]


    parents = []
        
    #choose the peasant parent
    roll_inf = rnd.uniform(0, t_fitness_inf)
    pinf_fitness = 0
    
    for i in range(split_point):
          pinf_fitness += fit_hash[i][0]
          if pinf_fitness >= roll_inf:
                parents.append(fit_hash[i][1])
                break;

    #choose the rich parent
    roll_sup = rnd.uniform(0, t_fitness_sup)
    psup_fitness = 0

    for i in range(split_point, len(fit_hash)):
          psup_fitness+= fit_hash[i][0]
          if psup_fitness >= roll_sup:
                parents.append(fit_hash[i][1])
                break;
    
    return parents
    
    # roll = rnd.uniform(t_fitness / 5, t_fitness)
    # # roll = rnd.uniform(0, t_fitness)
    # p_fitness = 0
    # fitness = 0

    # for i in range(p_size):
    #     fitness = fit_hash[i][0]
    #     p_fitness += fitness
    #     if p_fitness >= roll:
    #         return fit_hash[i][1]

    # raise NameError("roulette isnt working what")


def do_gen(profs, clases_index, clases, p_size, co_rate, mu_rate, gens):
    #not necessary but useful for somethign else
    lns_test()
    
    population = rnd_popul(p_size, profs, clases_index, clases)
    find_champ(population)

    gen_count = 0

    fit_hash = []

    succs = []
    start = tm.time()

    while gen_count < gens:
        start2 = tm.time()

        
        # t_fitness = 0
        # fitness = 0
        # for i in range(p_size):
        #     fitness = population[i].score
        #     fit_hash.append((fitness, i))
        #     t_fitness += fitness

        # print("\nthis gen", gen_count, "has", t_fitness / p_size, " avg fitnerinos")

        # # doesnt seem to make a huge difference in result
        # fit_hash.sort(key=lambda tup: tup[0])



        
        avg_parent_score = 0
        
        while len(succs) < p_size:
            parents = roulette(population, 0.6)
            index1 = parents[0]
            index2 = parents[1]
            
            # index1 = roulette(p_size, fit_hash, t_fitness)
            # index2 = roulette(p_size, fit_hash, t_fitness)

            parent1 = population[index1]
            parent2 = population[index2]

            avg_parent_score += parent1.score + parent2.score

            children = cross_over(
                profs, clases_index, clases, parent1, parent2, co_rate
            )

            mutation(profs, clases_index, clases, parent1, parent2, mu_rate)
            succs.append(children[0])
            succs.append(children[1])

        population = succs
        succs = []
        fit_hash.clear()

        this_time = tm.time() - start2
        find_champ(population)
        print("generation", gen_count, "took:", this_time)
        gen_count += 1

        print("\nMEASUREMENTS_____________________")
        print("avg parent score", avg_parent_score / p_size)
        print("END MEASUREMENTS_________________\n")

    print("finished genetic recombination!")
    t_time = tm.time() - start
    find_champ(population)
    print("found in", t_time, "avg gen took", t_time / gens)


# increase mutation probability gradually
do_gen(some_profs, some_clases_index, some_clases, 300, 0.7, 0.001, 800)
