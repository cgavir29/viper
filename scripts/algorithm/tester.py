from .profesor import Profesor
from .clase import Clase
from .horario import Horario
from .escuela import Escuela
from .lns import do_lns, greedy_sol, gen_rndsol, get_clases_index
from .gacomp import do_gen


print("REMINDERS: \n")
print(
    ">currently, youve established that is the prof is overused, he cant teach anymore, both in is_avail and eval_prof, but only the one in is_avail counts\n"
)

print(">make a solution checker\n")
print(
    ">split is_avail method into 2, one only check schedule (for cand assignment) the other one considers venues\n"
)

def test_is_avail():
    print("TEST IS AVAIL--------------------------------------------\n")

    esc1 = Escuela("some esc")
    print(esc1.get_clases().items())
    
    new_prof = Profesor("test")
    new_prof.add_sede("p")
    new_prof.add_sede("l")
    new_prof.add_sede("s")
    new_prof.set_avail(['l', 'm','w','j', 'v'], list(range(6,20)))
    
    new_clase1 = Clase("hellO1", sede = "l")
    new_clase1.set_horario(['l', 'm'], [14])
    esc1.add_clase(new_clase1)
    
    new_clase2 = Clase("hellO2", sede = "p")
    new_clase2.set_horario(['l', 'm'], [10,11])    
    esc1.add_clase(new_clase2)
    
    new_clase3 = Clase("hellO3", sede = "s")
    new_clase3.set_horario(['l', 'm'], [16, 17, 18])
    esc1.add_clase(new_clase3)
    
    new_prof.add_clase(new_clase1)
    print(esc1.get_clases().items())
    
    print(new_prof.get_horario())
    print("Clase2,", new_prof.sede_check_2(new_clase2, esc1))
    print("Clase3,", new_prof.sede_check_2(new_clase3, esc1))
    print("----------------------------------------------------------\n")




def run_greedy(esc, clases_index): 
    print("GRRRRREEEEEEEEEEEEEEEEEEEEEED---------------------------------")
    greed_sol = greedy_sol(esc, clases_index)
    greed_sol.print_info()
    print("--------------------------------------------------------------\n")

    
def run_pure_lns(esc):
    print("RND SOL INI---------------------------------------------------")
    rnd_sol = gen_rndsol(esc)
    rnd_sol.print_info()
    print("--------------------------------------------------------------\n")

    for i in range(1000):
        do_lns(rnd_sol,esc, 50, 110)

    rnd_sol.print_info()
    
def run_genetic_alg(esc, clases_index):
    print("Starting GA fool--------------------------------------------------")
    champ_sol = do_gen(esc, clases_index, 300, 0.7, 0.005, 1200)
    champ_sol.print_asigs()
    print("----------------------------------------------------------\n")
    

    
def algorith_tester():
    print("TESTING ALGORITHMS WITH RANDOM PROFS---------------------\n")
    rnd_esc = gen_rndesc(
        300,
        0.75,
        1,
        0.5,
        ["simevi", "microteach", "prom_eval", "pdp_cum", "estatus"],
        ["u", "s", "l", "b", "r", "p"],
    )

    clases_index = get_clases_index(rnd_esc)
    rnd_esc.print_info()
    run_greedy(rnd_esc, clases_index)
    run_pure_lns(rnd_esc)
    run_genetic_alg(rnd_esc, clases_index)


# test_is_avail()    
algorith_tester()
