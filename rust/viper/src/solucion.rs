extern crate hashbrown;

use crate::{clase::Clase, profesor::Profesor};
use hashbrown::{HashMap, HashSet};

pub struct Solucion {
    profs: HashMap<String, (Profesor, i32)>,
    clase_prof: HashMap<String, (String, f64)>,
    score: f64,
    active_profs: i32,
    holes: HashSet<String>,
}

impl Solucion {
    pub fn new() -> Solucion {
        //add a "nocand" prof (SHUTUP OK)
        let mut no_cand = Profesor::new("nocand".to_string());
        no_cand.set_vars("nocand", -10000);
        let mut solmap = HashMap::new();
        solmap.insert(no_cand.get_id().to_string(), (no_cand, 0));

        Solucion {
            profs: solmap,
            clase_prof: HashMap::new(),
            score: 0.0,
            active_profs: 0,
            holes: HashSet::new(),
        }
    }

    pub fn print_info(&self) {
        println!("active profs {}", self.get_actprofs());
        println!("score {}", self.get_score());
        println!(
            "holes {} conf {}",
            self.get_holes().len(),
            self.count_holes()
        );

    }

    pub fn get_score(&self) -> f64 {
        self.score
    }

    pub fn get_actprofs(&self) -> i32 {
        self.active_profs
    }

    pub fn get_prof(&self, profid: &str) -> Option<&Profesor> {
        let tup = self.profs.get(profid);
        match tup {
            Some(x) => Some(&(x.0)),
            None => None,
        }
    }

    pub fn get_profs(&self) -> &HashMap<String, (Profesor, i32)> {
        &(self.profs)
    }

    pub fn add_prof(&mut self, prof: &Profesor) {
        self.profs
            .insert(prof.get_id().to_string(), (prof.copy_self(), 0));
    }

    pub fn get_clprofs(&self) -> &HashMap<String, (String, f64)> {
        &(self.clase_prof)
    }

    pub fn get_clprof(&self, claseid: &str) -> Option<&(String, f64)> {
        match self.clase_prof.get(claseid) {
            Some(x) => Some(x),
            None => None,
        }
    }

    pub fn del_clprof(&mut self, clase: &Clase) {
        // println!("YOU HAVENT CHECKED IF DEL_CLPROF WORKS WELLLLLL");

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
    }

    pub fn set_clprof(&mut self, clase: &Clase, profid: &str) {
        if profid == "nocand" {
            self.add_hole(clase);
        } else {
            self.del_clprof(clase); //remove previous teacher
                                    //i dont use add_hole because it would instantly be patched

            self.del_hole(clase); //remove it from holes if it was there

            //get the replacement
            let prof_tup = self.profs.get_mut(profid).unwrap();
            (prof_tup.1) += 1; //add a class to it
            if (prof_tup.1) == 1 {
                //if he was inactive activate him
                self.active_profs += 1;
            }

            let punt = clase.eval_prof(&prof_tup.0); //prof score
            self.score += punt as f64; //add new prof score
            self.clase_prof
                .insert(clase.get_id().to_string(), (profid.to_string(), punt)); //insert into clase_prof
            (prof_tup.0).add_clase(clase);
        }
    }

    pub fn get_holes(&self) -> &HashSet<String> {
        &self.holes
    }

    pub fn add_hole(&mut self, clase: &Clase) {
        self.clase_prof
            .insert(clase.get_id().to_string(), ("nocand".to_string(), 0.0));
        self.holes.insert(clase.to_string());
    }

    pub fn del_hole(&mut self, clase: &Clase) {
        self.holes.remove(clase.get_id());
    }

    pub fn count_holes(&self) -> i32 {
        let sol_asigs = self.clase_prof.keys(); //class id's
        let mut num = 0;
        let nocand = String::from("shiuhiuhi");
        for i in sol_asigs {
            let tup = self.get_clprof(i).unwrap();
            num = if &tup.0 == "nocand" { num + 1 } else { num };
        }
        num
    }
}
