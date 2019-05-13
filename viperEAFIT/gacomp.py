import random as rnd, solucion as sol, copy, time as tm, simdata as sm, profesor as pr, horario as hr
import lns
import copy

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


def find_champ(popul, printit = False):
    champ = max(popul, key=lambda a: a.nom_score)
    if printit:
        champ.print_info()
        # champ.print_to_file("champ.out"); 
    # print(type(champ))
    return champ

def rnd_popul(size, esc):
    ini = tm.time()
    population = []
    for i in range(size):
        ini_ind = tm.time()
        population.append(lns.gen_rndsol(esc))
        print("solution", i, "done in", tm.time() - ini_ind, end="\r")
    return population

def cross_over(esc, clases_index, parent1, parent2, rate):

    roll = rnd.random()
    child1 = sol.Solucion()
    child2 = sol.Solucion()
    if roll <= rate:
        co_point = rnd.randint(1, len(parent1.clase_prof) - 2)
        index = 0
        for claseid in clases_index:
            clase = esc.get_clase(claseid)

            info1 = parent1.get_clprof(clase.iden)
            prof1 = esc.get_prof(info1[0])

            info2 = parent2.get_clprof(clase.iden)
            prof2 = esc.get_prof(info2[0])

            if index <= co_point:
                index += 1
                if child1.get_prof(prof1.iden) == None:
                    child1.add_prof(esc.get_prof(prof1.iden))
                child1.set_clprof(clase, prof1.iden)

                if child2.get_prof(prof2.iden) == None:
                    child2.add_prof(esc.get_prof(prof2.iden))
                child2.set_clprof(clase, prof2.iden)

            else:
                index += 1

                p2c1prof = child1.get_prof(prof2.iden)
                
                if p2c1prof == None:
                    p2c1prof = esc.get_prof(prof2.iden)

                if not p2c1prof.is_avail(clase, esc):
                    child1.add_hole(clase)
                    p2c1prof = None
                    # p2c1prof = gene_repair(profs, clase, child1)
                    
                if p2c1prof != None:
                      if child1.get_prof(p2c1prof.iden) == None:
                            child1.add_prof(p2c1prof)
                            
                      child1.set_clprof(clase, p2c1prof.iden)

                      
                p1c2prof = child2.get_prof(prof1.iden)

                if p1c2prof == None:
                    p1c2prof = esc.get_prof(prof1.iden)

                if not p1c2prof.is_avail(clase, esc):
                    child2.add_hole(clase)
                    p1c2prof = None

                if p1c2prof != None:
                      if child2.get_prof(p1c2prof.iden) == None:
                            child2.add_prof(p1c2prof)
                            
                      child2.set_clprof(clase, p1c2prof.iden)

                      
        lns.do_lns(child1, esc, 30, 30)
        lns.do_lns(child2, esc, 30, 30)
        
        return (child1, child2)

    else:
        return (parent1, parent2)


def mutation(esc, clases_index, subject1, subject2, rate):
    roll = rnd.random()

    for claseid in clases_index:
        clase = esc.get_clase(claseid)
        if roll <= rate:
            prof = lns.rnd_gene_repair(esc, clase, subject1)
            if subject1.get_prof(prof.iden) == None:
                subject1.add_prof(prof)
            subject1.set_clprof(clase, prof.iden)
        roll = rnd.random()

        if roll <= rate:
            prof = lns.rnd_gene_repair(esc, clase, subject2)
            if subject2.profs.get(prof.iden) == None:
                subject2.add_prof(prof)
            subject2.set_clprof(clase, prof.iden)
        roll = rnd.random()


# 13918 13878 w sort 300 >200
# 13326 13161.51 wo sort 300 >200 seems to converge around 223


def roulette(population, split):
    #HARD SEGREGATION, SOFT SEGREGATION WOULD
    #ONLY AFFECT THE ROLL
    
    fit_hash = []
    for i in range(len(population)):
        fitness = population[i].nom_score
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


def do_gen(esc, clases_index, p_size, co_rate, mu_rate, gens):
    #not necessary but useful for somethign else
    
    population = rnd_popul(p_size, esc)

    gen_count = 0

    fit_hash = []

    succs = []
    start = tm.time()

    while gen_count < gens:
        start2 = tm.time()        
        avg_parent_score = 0
        
        succs.append(copy.deepcopy(find_champ(population)))
        while len(succs) < p_size:
            parents = roulette(population, 0.6)
            index1 = parents[0]
            index2 = parents[1]
            
            parent1 = population[index1]
            parent2 = population[index2]

            avg_parent_score += parent1.nom_score + parent2.nom_score

            children = cross_over(esc, clases_index, parent1, parent2, co_rate)

            mutation(esc, clases_index, children[0], children[1], mu_rate)
            succs.append(children[0])
            succs.append(children[1])
        
        population = succs
        succs = []
        fit_hash.clear()

        this_time = tm.time() - start2

        gen_count += 1
        print("\ngeneration", gen_count, "took:", this_time)        
        print("MEASUREMENTS_____________________")
        print("avg parent score", avg_parent_score / p_size)
        find_champ(population, True)
        print("END MEASUREMENTS_________________\n")

    print("finished genetic recombination!")
    t_time = tm.time() - start
    print("found in", t_time, "avg gen took", t_time / gens)
    return find_champ(population)


# increase mutation probability gradually
