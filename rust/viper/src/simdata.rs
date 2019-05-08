extern crate hashbrown;
use crate::{clase::Clase, curso::Curso, escuela::Escuela, horario::Horario, profesor::Profesor};
use hashbrown::HashMap;
use rand::Rng;
use std::cmp::Ordering;

fn gen_rnd_str(size: usize) -> String {
    let mut rnd = rand::thread_rng();
    let mut rndstr = String::new();
    for _ in 0..size {
        let c = rnd.gen_range(97, 122) as u8;
        rndstr.push(c as char);
    }
    // println!("{}", rndstr);
    rndstr
}

fn gen_courses(esc: &mut Escuela) {
    for lvl in 1..6 {
        if lvl <= 3 {
            for letter in vec!["A", "B", "C"] {
                let mut curso = Curso::new("".to_string());
                curso.add_reqr("enga1");
                curso.set_id(lvl.to_string() + letter);
                esc.add_curso(curso);
            }
        } else {
            let mut curso = Curso::new("".to_string());
            curso.add_reqr("enga1");
            curso.set_id(lvl.to_string());
            esc.add_curso(curso);
        }
    }

    for lvl in 6..11 {
        let mut curso = Curso::new(lvl.to_string());
        curso.add_reqr("enga2");
        esc.add_curso(curso);
    }

    for lvl in 11..15 {
        let mut curso = Curso::new(lvl.to_string());
        curso.add_reqr("engb1");
        esc.add_curso(curso);
    }

    for lvl in 15..20 {
        if lvl <= 3 {
            for letter in vec!["A", "B", "C", "D"] {
                let mut curso = Curso::new("".to_string());
                curso.set_id(lvl.to_string() + letter);
                curso.add_reqr("engb2");
                esc.add_curso(curso);
            }
        } else {
            let mut curso = Curso::new("".to_string());
            curso.set_id(lvl.to_string());
            curso.add_reqr("engb2");
            esc.add_curso(curso);
        }
    }
}

fn create_clase<'a>(
    dias: &Vec<&str>,
    horas: &Vec<i32>,
    sede: &str,
    clase_ind: i32,
    curso: &str,
) -> Clase {
    let mut cs1 = Clase::new((clase_ind.to_string() + sede) + curso, curso, sede);
    cs1.set_horario(dias, horas);
    cs1
}

fn generate_clases(esc: &mut Escuela) -> Vec<Clase> {
    let mut clases = Vec::new();
    let mut clase_ind = 0;
    let mut dias: Vec<&str> = Vec::new();
    let mut horas: Vec<i32> = Vec::new();
    for crs in esc.get_cursos().values() {
        // println!("{} {} ", crs, clase_ind);
        let curso = crs.get_id();

        dias = vec!["l", "w"];
        horas = vec![18, 19];
        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "l", clase_ind, curso));

        dias = vec!["m", "j"];
        horas = vec![10, 11];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        horas = vec![12, 13];
        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        horas = vec![18, 19];
        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "l", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "s", clase_ind, curso));

        dias = vec!["w", "v"];

        horas = vec![12, 13];
        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "s", clase_ind, curso));

        dias = vec!["s"];
        horas = vec![8, 9, 10, 11];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "b", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "r", clase_ind, curso));

        horas = vec![13, 14, 15, 16];
        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "l", clase_ind, curso));

        dias = vec!["l", "w", "v"];
        horas = vec![6, 7];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "l", clase_ind, curso));

        horas = vec![12, 13];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "s", clase_ind, curso));

        horas = vec![10, 11];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        horas = vec![18, 19];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "s", clase_ind, curso));

        dias = vec!["m", "j"];
        horas = vec![6, 7, 8];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "l", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "s", clase_ind, curso));

        horas = vec![9, 10, 11];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "s", clase_ind, curso));

        dias = vec!["w", "v"];
        horas = vec![6, 7, 8];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        horas = vec![9, 10, 11];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "l", clase_ind, curso));

        dias = vec!["l", "m", "w", "j", "v"];
        horas = vec![6, 7];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "s", clase_ind, curso));

        horas = vec![8, 9];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "l", clase_ind, curso));

        horas = vec![10, 11];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        horas = vec![12, 13];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        dias = vec!["l", "m", "w", "j"];

        horas = vec![6, 7, 8];

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "u", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "l", clase_ind, curso));

        clase_ind += 1;
        clases.push(create_clase(&dias, &horas, "s", clase_ind, curso));
    }

    clases
}

fn get_esc_sch(clases: &Vec<Clase>) -> Vec<&Horario> {
    let mut class_schs: Vec<&Horario> = Vec::new();
    for clase in clases {
        let hor_class = clase.get_horario();

        let mut included = false;
        for sch in &class_schs {
            if hor_class.equal_to(*sch) {
                // println!("hiiii");
                included = true;
                break;
            }
        }

        if !included {
            class_schs.push(hor_class);
        }
    }
    println!("there are {} different schs", class_schs.len());
    class_schs
}

fn gen_rnd_hor(prof: &mut Profesor, max_h: i32) {
    let mut tot_h = max_h;
    let mut rnd = rand::thread_rng();
    let mut dias = vec!["l", "m", "w", "j", "v", "s"];
    while tot_h > 0 {
        rnd.shuffle(&mut dias);
        for dia in &dias {
            let mut num_hours = rnd.gen_range(2, 8);
            tot_h -= num_hours;
            if tot_h <= 0 {
                break;
            }
            let mut start: i32 = rnd.gen_range(6, 22 - num_hours);
            let mut day_sch: Vec<i32> = Vec::new();

            while num_hours > 0 {
                day_sch.push(start);
                start += 1;
                num_hours -= 1;
            }
            prof.set_avail(&vec![dia.to_string()], &day_sch);
        }
    }
    // println!("{}", prof.get_horario().count_avail());
}

fn gen_rnd_profs(
    amount: i32,
    certper: f64,
    sedper: f64,
    classper: f64,
    vars: &Vec<&str>,
    sedes: &Vec<&str>,
    clases: &Vec<Clase>,
) -> Vec<Profesor> {
    let all_schs = get_esc_sch(clases);
    let mut rnd = rand::thread_rng();
    let mut profesores: Vec<Profesor> = Vec::new();
    let mut full_schs = 0;
    let mut hr_avg = 0;
    let certs_cat = ["enga1", "enga2", "engb1", "engb2"];

    for i in 0..amount {
        let mut prof = Profesor::new(i.to_string());

        for esc_sch in &all_schs {
            let roll: f64 = rnd.gen();
            if roll < classper {
                prof.copy_avail_sch(esc_sch);
            }
        }

        // gen_rnd_hor(&mut prof, hr_len); //generates random schs for the teachers

        let hr_len = prof.get_horario().count_avail();
        hr_avg += hr_len;

        for reqr in &certs_cat {
            let roll: f64 = rnd.gen();
            if roll < certper {
                prof.add_reqr(reqr);
            }
        }

        for sede in sedes {
            let roll: f64 = rnd.gen();
            if roll < sedper {
                prof.add_sede(*sede);
            }
        }
        for var in vars {
            let roll: f64 = rnd.gen();
            if roll < 0.2 {
                prof.set_vars((*var), rnd.gen_range(0, 1));
            } else if roll < 0.9 {
                prof.set_vars((*var), rnd.gen_range(2, 4));
            } else {
                prof.set_vars(*var, 5);
            }
        }
        profesores.push(prof);
    }

    println!("hr average {}", hr_avg / amount);
    profesores
}

pub fn create_rnd_esc(
    prof_amount: i32,
    certper: f64,
    sedper: f64,
    classper: f64,
    vars: &Vec<&str>,
    sedes: &Vec<&str>,
) -> Escuela {
    let mut rnd_esc = Escuela::new("hi".to_string());
    let escref = &mut rnd_esc;
    gen_courses(escref);
    let mut clases = generate_clases(escref);
    let mut profs = gen_rnd_profs(prof_amount, certper, sedper, classper, vars, sedes, &clases);

    let temp_fn = |a: &Profesor, b: &Profesor| -> Ordering {
        if a.get_score() > b.get_score() {
            Ordering::Less
        } else {
            Ordering::Greater
        }
    };

    // CURRENTLY SORTING HERE
    profs.sort_by(temp_fn);

    for (mut clase) in clases.drain(..) {
        // println!("{} \n", clase);
        for prof in &profs {
            if clase.can_teach(prof, escref) {
                clase.add_cand(prof);
            }
        }

        escref.add_clase(clase);
    }

    for prof in profs.drain(..) {
        // println!("{}", prof.get_horario());
        escref.add_prof(prof);
    }

    rnd_esc
}
