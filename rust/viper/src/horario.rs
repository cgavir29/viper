extern crate hashbrown;
use hashbrown::HashMap;

pub struct Horario {
    diario: HashMap<String, HashMap<i32, String>>,
    total_h: i32,
}

impl std::fmt::Display for Horario {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        let mut repr = String::new();
        
        //i guess they wont be traching classes on sundays from now on lmao
        let better_days = vec!["l", "m", "w", "j", "v", "s"];
        for d in better_days {
            repr.push_str(d);
            repr.push_str("   ");
            let class_num = (self.diario.get(d)).unwrap();
            if class_num.len() > 0 {
                let mut day_cs = String::new();
                
                let mut pairs: Vec<(&i32, &String)> = class_num.iter().collect();
                pairs.sort(); //this workds even if its &i32 ig
                for (h, c) in pairs {
                    day_cs.push_str(&h.to_string());
                    day_cs.push_str(": ");
                    day_cs.push_str(c);
                    day_cs.push_str(" ");
                }

                repr.push_str(&day_cs);
                repr.push_str("    \n");
            }
        }

        write!(f, "{}", repr)
    }
}

impl Horario {
    pub fn new() -> Horario {
        let mut basic_diario = HashMap::new();
        basic_diario.insert("l".to_string(), HashMap::new());
        basic_diario.insert("m".to_string(), HashMap::new());
        basic_diario.insert("w".to_string(), HashMap::new());
        basic_diario.insert("j".to_string(), HashMap::new());
        basic_diario.insert("v".to_string(), HashMap::new());
        basic_diario.insert("s".to_string(), HashMap::new());
        
        Horario {
            diario: basic_diario,
            total_h: 0,
        }
    }

    pub fn get_diario(&self) -> &HashMap<String, HashMap<i32, String>> {
        &(self.diario)
    }

    pub fn count_avail(&self) -> i32 {
        let mut zeros = 0;
        let dia_cop = (self.diario).keys();

        for d in dia_cop {
            let day = (self.diario.get(d)).unwrap().values();

            for h in day {
                if h == "0" {
                    zeros += 1;
                }
            }
        }
        zeros
    }

    pub fn get_dia(&self, dia: &str) -> &HashMap<i32, String> {
        (self.diario).get(dia).unwrap()
    }

    pub fn get_horario(&self, dia: &str, hora: i32) -> &str {
        (self.diario).get(dia).unwrap().get(&hora).unwrap()
    }
    pub fn set_single(&mut self, dia: &str, hora: i32, val: &str) {
        self.diario.get_mut(dia).unwrap().insert(hora, val.to_string());
    }
    
    pub fn set_horario(&mut self, dia: &str, horas: &Vec<i32>, val: &str, state: bool) {
        if state {
            //Add a hashmap in the given day if it hasnt been added yet
            for h in horas {
                // let a: &mut HashMap<i32, String> = (self.diario).get_mut(dia).unwrap();
                
                (self.diario)  //HashMap<String, HashMap<i32, String>>
                    .get_mut(dia)
                    .unwrap()
                    .insert(*h, val.to_string());
                if val != "0" {
                    self.total_h += 1;
                }
            }
        } else {
            for h in horas {
                (self.diario)
                    .get_mut(dia)
                    .unwrap()
                    .insert(*h, String::from("0"));
                self.total_h -= 1;
            }
        }
    }
}
