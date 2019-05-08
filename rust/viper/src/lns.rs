extern crate hashbrown;
use hashbrown::HashSet;

use crate::{
    clase::Clase, curso::Curso, escuela::Escuela, horario::Horario, profesor::Profesor,
    simdata::create_rnd_esc, solucion::Solucion,
};
use rand::Rng;
use std::cmp::Ordering;

fn sort_keys<'a>(clases_index: &mut Vec<&'a str>, esc: &Escuela) {
    let temp_fn = |a: &&str, b: &&str| -> Ordering {
        let clase_a = esc.get_clase(*a);
        let clase_b = esc.get_clase(*b);
        if clase_a.get_cands().len() > clase_b.get_cands().len() {
            Ordering::Greater
        } else {
            Ordering::Less
        }
    };

    clases_index.sort_by(temp_fn);
}

fn rnd_gene_repair(esc: &Escuela, clase: &Clase, sol: &Solucion) -> String {
    let mut rnd = rand::thread_rng();
    let mut cand_id = &clase
        .get_cands()
        .get(0)
        .expect("a class without cands UwU")
        .0;

    let teacher_amount = clase.get_cands().len();
    let mut used_profs: HashSet<usize> = HashSet::new();
    used_profs.reserve(teacher_amount);

    let mut prof_op: Option<&Profesor> = sol.get_prof(cand_id);
    let mut prof: &Profesor = match prof_op {
        Some(_) => prof_op.unwrap(),
        None => esc.get_prof(cand_id),
    };

    let teacher_amount = clase.get_cands().len();
    // println!("teacher amount {}", teacher_amount);
    let mut index = rnd.gen_range(0, teacher_amount);

    while !prof.is_avail(clase.get_horario()) || used_profs.contains(&index) {
        // println!("index {}", index);
        if used_profs.len() >= teacher_amount {
            return "nocand".to_string();
        }

        cand_id = &clase.get_cands().get(index).unwrap().0;
        prof_op = sol.get_prof(cand_id);

        prof = match prof_op {
            Some(_) => prof_op.unwrap(),
            None => esc.get_prof(cand_id),
        };
        used_profs.insert(index);
        index = rnd.gen_range(0, teacher_amount);
    }

    prof.get_id().to_string()
}

fn gen_rndsol(esc: &Escuela, clases_index: &Vec<&str>) -> Solucion {
    let mut solb = Solucion::new();
    let mut prof_id: String;
    let mut prof: Option<&Profesor>;

    for cla_id in clases_index {
        let cla = esc.get_clase(cla_id);
        prof_id = rnd_gene_repair(esc, cla, &solb);
        prof = solb.get_prof(&prof_id);

        match prof {
            None => solb.add_prof(esc.get_prof(&prof_id)),
            _ => (),
        };

        solb.set_clprof(cla, &prof_id);
    }

    solb
}

fn gene_repair_cands(esc: &Escuela, clase: &Clase, sol: &Solucion) -> String {
    let mut rnd = rand::thread_rng();
    let mut cand_id = &clase
        .get_cands()
        .get(0)
        .expect("a class without cands UwU")
        .0;

    let mut prof_op: Option<&Profesor> = sol.get_prof(cand_id);

    let mut prof: &Profesor = match prof_op {
        Some(_) => prof_op.unwrap(),
        None => esc.get_prof(cand_id),
    };

    let teacher_amount = clase.get_cands().len();
    // println!("teacher amount {}", teacher_amount);
    let mut index = 0;

    while !prof.is_avail(clase.get_horario()) {
        // println!("index {}", index);
        if index >= teacher_amount {
            return "nocand".to_string();
        }
        cand_id = &clase.get_cands().get(index).expect("out of bounds?????").0;
        prof_op = sol.get_prof(cand_id);

        prof = match prof_op {
            Some(_) => prof_op.unwrap(),
            None => esc.get_prof(cand_id),
        };

        index += 1;
    }
    prof.get_id().to_string()
}

fn greedy_sol(esc: &Escuela, clases_index: &Vec<&str>) -> Solucion {
    let mut solb = Solucion::new();
    let mut prof_id: String;
    let mut prof: Option<&Profesor>;

    for cla_id in clases_index {
        let cla = esc.get_clase(cla_id);
        prof_id = gene_repair_cands(esc, cla, &solb);
        prof = solb.get_prof(&prof_id);

        match prof {
            None => solb.add_prof(esc.get_prof(&prof_id)),
            _ => (),
        };

        solb.set_clprof(cla, &prof_id);
    }

    solb
}

fn destroy_by_classnum(sol: &Solucion, amount_des: i32, esc: &Escuela) {}

pub fn test_lns() {
    println!("REMEMBER TO SORT CANDIDATES, SORTING IN SIMDATA RN");
    let mut esc = create_rnd_esc(
        300,
        0.75,
        1.0,
        0.5,
        &vec![
            "simevi",
            "microteaching",
            "promedio_eval",
            "pdp_cum",
            "estatus",
        ],
        &vec!["u", "s", "l", "b", "r", "p"],
    );

    let mut clases_index: Vec<&str> = Vec::new();
    for i in esc.get_clases().keys() {
        clases_index.push(i);
    }

    sort_keys(&mut clases_index, &esc);

    println!("\ngenrating random solution");
    let rnd_sol = gen_rndsol(&esc, &clases_index);
    rnd_sol.print_info();

    
    println!("\ngrreeeeeeeeeeeeeeeeeeed");
    let greed = greedy_sol(&esc, &clases_index);
    greed.print_info();
    // println!("{:?}", greed.get_clprofs();
}
