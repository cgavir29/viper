from .horario import Horario
from .tester import run_pure_lns, run_genetic_alg, get_clases_index, run_greedy
from .lns import balance_class_assigs
# from simdata import gen_rndesc


def check_congruent_avail(sol, esc):
    print("CHECKING THAT THE SCHEDULES MATCH")
    for (prof, _) in sol.get_profs().values():
        print(prof.get_id(), end="\r")
        prof_hr = prof.get_horario()
        og_prof = esc.get_prof(prof.get_id())
        og_prof_hr = og_prof.get_horario()
        if not prof_hr.is_congruent_with(
            og_prof_hr
        ) and not og_prof_hr.is_congruent_with(prof_hr):
            print(prof_hr)
            print("----------------------------")
            print(og_prof_hr)
            print("YOU DUN FUUUUUUUUUUUCKED NIGGAGAGGAGAGAGA")
    print("DONE")



def check_num_classh(sol, esc):
    for (clase_id, prof_tup) in sol.get_clprofs().items():
        clase = esc.get_clase(clase_id)
        prof = sol.get_prof(prof_tup[0])
        print(clase.get_horario().count_instances_of(clase_id))
        print(prof.get_horario().count_instances_of(clase_id))
        print("-------------------------------------------------")




    
def check_solution(sol=None, esc=None):
    rnd_esc = gen_rndesc(
        300,
        0.75,
        1,
        0.5,
        ["simevi", "microteach", "prom_eval", "pdp_cum", "estatus"],
        ["u", "s", "l", "b", "r", "p"],
    )
    clases_index = get_clases_index(rnd_esc)
    greed_sol = run_greedy(rnd_esc, clases_index)
    
    lns_sol = run_pure_lns(rnd_esc)
    
    balance_class_assigs(lns_sol, rnd_esc, clases_index)
    # check_congruent_avail(lns_sol, rnd_esc)
    # check_num_classh(lns_sol, rnd_esc)
    lns_sol.print_info()
    
    # gen_sol = run_genetic_alg(rnd_esc, clases_index, gens = 600, pop_size = 300)
    # # check_congruent_avail(gen_sol, rnd_esc)
    # # check_num_classh(gen_sol, rnd_esc)
    # balance_class_assigs(gen_sol, rnd_esc, clases_index)
    
check_solution()
