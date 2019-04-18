extern crate hashbrown;
use crate::{clase::Clase, curso::Curso, escuela::Escuela, horario::Horario, profesor::Profesor};
use hashbrown::HashMap;
use rand::Rng;

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

fn gen_courses() -> Vec<Curso> {
    let mut cursos = Vec::new();
    for lvl in 1..6 {
        let mut curso = Curso::new("".to_string());

        if lvl <= 3 {
            for letter in vec!["A", "B", "C"] {
                curso.set_id(lvl.to_string() + letter);
            }
        } else {
            curso.set_id(lvl.to_string());
        }

        curso.add_reqr("enga1");
        cursos.add_curso(curso);
    }

    for lvl in 6..11 {
        let mut curso = Curso::new(lvl.to_string());
        curso.add_reqr("enga2");
        cursos.add_curso(curso);
    }

    for lvl in 11..15 {
        let mut curso = Curso::new(lvl.to_string());
        curso.add_reqr("engb1");
        cursos.add_curso(curso);
    }

    for lvl in 15..20 {
        let mut curso = Curso::new("".to_string());

        if lvl <= 3 {
            for letter in vec!["A", "B", "C", "D"] {
                curso.set_id(lvl.to_string() + letter);
            }
        } else {
            curso.set_id(lvl.to_string());
        }

        curso.add_reqr("engb2");
        cursos.add_curso(curso);
    }

    cursos
}

fn create_clase<'a>(
    dias: &Vec<&str>,
    horas: &Vec<i32>,
    sede: &str,
    clase_ind: i32,
    curso: &'a Curso,
) -> Clase <'a> {
    let mut dias_new = Vec::new();
    for dia in dias {
        dias_new.push(dia.to_string());
    }

    let mut cs1 = Clase::new((clase_ind.to_string() + sede) + curso.get_id(), curso, sede);
    cs1.set_horario(dias, horas);
    cs1
    
}

fn generate_clases(cursos: &Vec<Curso>) -> Vec<Clase> {
    for curso in cursos {
        

     }
}

pub fn create_rnd_esc(){
}
