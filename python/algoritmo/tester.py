from simdata import gen_rndesc
from profesor import Profesor
from horario import Horario
from lns import do_lns, greedy_sol, gen_rndsol, get_clases_index
from gacomp import do_gen



rnd_esc = gen_rndesc(300, 0.75, 1, 0.5, ["simevi", "microteach", "prom_eval", "pdp_cum", "estatus"], ["u", "s", "l", "b", "r", "p"])

clases_index = get_clases_index(rnd_esc)
rnd_esc.print_info()

print("GRRRRREEEEEEEEEEEEEEEEEEEEEED---------------------------------")
greed_sol = greedy_sol(rnd_esc,clases_index)
greed_sol.print_info()
print("--------------------------------------------------------------\n")

print("RND SOL INI---------------------------------------------------")
rnd_sol = gen_rndsol(rnd_esc)
rnd_sol.print_info()
print("--------------------------------------------------------------\n")


# for i in range(1000):
#     do_lns(rnd_sol, rnd_esc, 80, 85);

# rnd_sol.print_info()
print("Starting GA fool--------------------------------------------------")


do_gen(rnd_esc, clases_index, 300, 0.7, 0.06, 800)
