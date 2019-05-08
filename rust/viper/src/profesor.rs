extern crate hashbrown;
use crate::clase::Clase;
use crate::horario::Horario;
use hashbrown::{HashMap, HashSet};

pub struct Profesor {
    iden: String,
    horario: Horario,
    reqr: HashSet<String>,
    variables: HashMap<String, i32>,
    sedes: HashSet<String>,
    max_horas: i32,
    score: f64,
}

impl std::fmt::Display for Profesor {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "prof {}", self.iden)
    }
}

impl Profesor {
    pub fn new(iden: String) -> Profesor {
        let mut variables = HashMap::new();
        variables.insert("simevi".to_string(), 0);
        variables.insert("microteaching".to_string(), 0);
        variables.insert("promedio_eval".to_string(), 0);
        variables.insert("pdp_cum".to_string(), 0);
        variables.insert("estatus".to_string(), 0);

        Profesor {
            iden,
            horario: Horario::new(),
            reqr: HashSet::new(),
            variables,
            sedes: HashSet::new(),
            max_horas: 0,
            score: 0.0,
        }
    }

    pub fn get_id(&self) -> &str {
        &(self.iden)
    }

    pub fn get_horario(&self) -> &Horario {
        &(self.horario)
    }

    pub fn eval_self(&mut self) {
        let mut score: f64 = 0.0;
        for var in self.variables.keys() {
            score += (*self.variables.get(var).unwrap()) as f64;
        }
        self.score = score;
    }

    pub fn copy_self(&self) -> Profesor {
        let mut sch = Horario::new();
        let this_diario = self.get_horario().get_diario();
        for dia in this_diario.keys() {
            let hour_class = self.get_horario().get_dia(dia).iter();
            for (hora, val) in hour_class {
                sch.set_single(dia, *hora, val);
            }
        }

        Profesor {
            iden: self.get_id().to_string(),
            horario: sch,
            reqr: HashSet::new(),
            variables: HashMap::new(),
            sedes: HashSet::new(),
            max_horas: self.max_horas,
            score: self.score,
        }
    }

    pub fn set_avail(&mut self, dias: &Vec<String>, horas: &Vec<i32>) {
        for dia in dias {
            self.horario.set_horario(dia, horas, "0", true);
        }
    }

    pub fn is_avail(&self, horariocl: &Horario) -> bool {
        let diario = horariocl.get_diario();
        for dia in diario.keys() {
            let horas = horariocl.get_dia(dia).keys();
            for hora in horas {
                if self.horario.get_horario(dia, *hora) != "0" {
                    return false;
                }
            }
        }
        return true;
    }

    pub fn add_clase(&mut self, clase: &Clase) {
        let class_sch = clase.get_horario();

        for dia in class_sch.get_diario().keys() {
            let daily = class_sch.get_dia(dia).iter();
            for (hora, clase) in daily {
                self.horario.set_single(dia, *hora, clase);
            }
        }
    }

    pub fn del_clase(&mut self, clase: &Clase) {
        let class_sch = clase.get_horario();

        for dia in class_sch.get_diario().keys() {
            let daily = class_sch.get_dia(dia).keys();
            for key in daily {
                self.horario.set_single(dia, *key, "0");
            }
        }
    }

    pub fn copy_avail_sch(&mut self, hor: &Horario) {
        let dias = hor.get_diario().keys();
                    let mut horas = Vec::new();
        for dia in dias {
            for time in hor.get_dia(dia).keys() {
                horas.push(*time);
            }
            
            self.horario.set_horario(dia, &horas, "0", true);
            horas.clear();
        }
    }

    pub fn get_reqr(&self) -> &HashSet<String> {
        &(self.reqr)
    }

    pub fn add_reqr(&mut self, reqr: &str) {
        self.reqr.insert(reqr.to_string());
    }

    pub fn get_vars(&self) -> &HashMap<String, i32> {
        &(self.variables)
    }

    pub fn set_vars(&mut self, key: &str, val: i32) {
        self.variables.insert(key.to_string(), val);
        //add this here so it updates
        self.eval_self();
    }

    pub fn get_sedes(&self) -> &HashSet<String> {
        &(self.sedes)
    }

    pub fn add_sede(&mut self, sede: &str) {
        self.sedes.insert(sede.to_string());
    }

    pub fn get_mhor(&self) -> i32 {
        self.max_horas
    }

    pub fn set_mhor(&mut self, val: i32) {
        self.max_horas = val;
    }

    pub fn get_score(&self) -> f64 {
        self.score
    }

    pub fn set_score(&mut self, val: f64) {
        self.score = val;
    }
}
