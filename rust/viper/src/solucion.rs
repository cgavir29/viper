extern crate hashbrown;
use crate::{clase::Clase, profesor::Profesor};
use hashbrown::HashMap;

pub struct Solucion {
    profs: HashMap<String, (Profesor, i32)>,
    clase_prof: HashMap<String, (String, f64)>,
    score: f64,
    active_profs: i32,
}

impl Solucion {
    pub fn new() -> Solucion {
        Solucion {
            profs: HashMap::new(),
            clase_prof: HashMap::new(),
            score: 0.0,
            active_profs: 0,
        }
    }
    pub fn get_prof(&self, profid: &str) -> &Profesor {
        let tup = self.profs.get(profid).unwrap();
        &(tup.0)
    }

    pub fn get_clprof(&self, claseid: &str) -> &(String, f64) {
        self.clase_prof.get(claseid).unwrap()
    }

    pub fn add_prof(&mut self, prof: &Profesor) {
        self.profs
            .insert(prof.get_id().to_string(), (prof.copy_self(), 0));
    }

    pub fn del_clprof(&mut self, clase: &Clase) {
        println!("YOU HAVENT CHECKED IF DEL_CLPROF WORKS WELLLLLL");

        let mut tup = self.clase_prof.get_mut(clase.get_id());

        match tup {
            Some(x) => {
                let mut tup = x;
                self.score -= tup.1 as f64;

                let prof_tup = self.profs.get_mut(&tup.0).unwrap();
                (prof_tup.0).del_clase(clase);
                (prof_tup.1) -= 1;
                self.clase_prof.remove(clase.get_id());

                if prof_tup.1 == 0 {
                    self.active_profs -= 1;
                }
            }
            None => {
                self.clase_prof.remove(clase.get_id());
            }
        }

        /*
                if tup != None {

                    self.score -= tup.1;
                    let prof_tup = self.profs.get_mut(tup.0);
                    (prof_tup.0).del_clase(clase);
                    (*prof_tup.1)-=1;
                    self.clase_prof.remove(clase.get_id());

                    if prof_tup.1 == 0 {
                        self.active_profs -= 1;
                    }

                }
        */
    }

    pub fn set_clprof(&mut self, clase: &Clase, profid: &str) {
        self.del_clprof(clase);

        let prof_tup = self.profs.get_mut(profid).unwrap();
        (prof_tup.1) += 1;
        if (prof_tup.1) == 1 {
            self.active_profs += 1;
        }

        let punt = clase.eval_prof(&prof_tup.0);
        self.score += punt as f64;
        self.clase_prof
            .insert(clase.get_id().to_string(), (profid.to_string(), punt));
        (prof_tup.0).add_clase(clase);
    }
}
