extern crate hashbrown;
use hashbrown::HashSet;

pub struct Curso {
    iden: String,
    reqr: HashSet<String>, 
}

impl std::fmt::Display for Curso {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "curso {}", self.iden)
    }
}

impl Curso {
    pub fn new(iden: String) -> Curso {
        Curso {iden, reqr: HashSet::new() }

    }

    pub fn get_id(&self) -> &str {
        &(self.iden)
    }

    pub fn set_id(&mut self, new_id: String) {
        self.iden = new_id

    }

    pub fn get_reqr(&self) -> &HashSet<String> {
        &(self.reqr)
    }
    
    pub fn add_reqr(&mut self, reqr: &str) {
        self.reqr.insert(reqr.to_string());
    }

}
