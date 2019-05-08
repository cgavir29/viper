use crate::curso::Curso;
use crate::escuela::Escuela;
use crate::horario::Horario;
use crate::profesor::Profesor;
pub struct Clase {
    iden: String,
    curso: String,
    sede: String,
    horario: Horario,
    profesor: Profesor,
    candidates: Vec<(String, f64)>,
}

impl std::fmt::Display for Clase {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "clase {}", self.iden)
    }
}

impl Clase {
    //i guess iden can be a string since its unique to a class
    // i think there no problem if this lfietime is different lmao
    pub fn new(iden: String, curso: &str, sede: &str) -> Clase {
        Clase {
            iden,
            curso: curso.to_string(),
            sede: sede.to_string(),
            horario: Horario::new(),
            profesor: Profesor::new("none".to_string()),
            candidates: Vec::new(),
        }
    }

    pub fn get_id(&self) -> &str {
        &(self.iden)
    }

    pub fn get_sede(&self) -> &str {
        &(self.sede)
    }
    
    pub fn get_prof(&self) -> &Profesor {
        if self.profesor.get_id() != "" {
            println!("no teacher assigned to {} yet nigga", self.iden);
        }

        &(self.profesor)
    }

    pub fn set_prof(&mut self, prof: &Profesor) {
        self.profesor = prof.copy_self();
    }

    pub fn get_horario(&self) -> &Horario {
        &(self.horario)
    }

    pub fn set_horario(&mut self, dias: &Vec<&str>, horas: &Vec<i32>) {
        for dia in dias {
            self.horario.set_horario(*dia, horas, &self.iden, true)
        }
    }

    pub fn get_cands(&self) -> &Vec<(String, f64)> {
        &(self.candidates)
    }

    pub fn add_cand(&mut self, prof: &Profesor) {
        self.candidates
            .push((prof.get_id().to_string(), self.eval_prof(prof)));
    }

    pub fn eval_prof(&self, prof: &Profesor) -> f64 {
        //TODO PROPERLY
        prof.get_score()
    }

    pub fn can_teach(&self, prof: &Profesor, esc: &Escuela) -> bool {
        
        
        if !prof.get_sedes().contains(&self.sede) {
            // println!("doesnt have sedes");
            return false;
        }





        
        if !prof.is_avail(&self.horario) {
            // println!("doesnt have hours");
            return false;
        }

        //i give up tryna make curso a ref

        let this_curso = esc.get_curso(&self.curso);

        for r in this_curso.get_reqr() {
            if !prof.get_reqr().contains(r) {
                
                // println!("{} doesnt have certs {}", prof, r);
                return false;
            }
        }
        return true;
    }
}
