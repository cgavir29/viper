extern crate hashbrown;
use crate::clase::Clase;
use crate::curso::Curso;
use crate::profesor::Profesor;
use hashbrown::{HashMap, HashSet};
use rand::Rng;

pub struct Escuela {
    name: String,
    profs: HashMap<String, Profesor>,
    clases: HashMap<String, Clase>,
    cursos: HashMap<String, Curso>,
}

impl Escuela{
    // i think there no problem if this lfietime is different lmao
    pub fn new(name: String) -> Escuela {
        Escuela {
            name,
            profs: HashMap::new(),
            clases: HashMap::new(),
            cursos: HashMap::new(),
        }
    }

    pub fn get_profs(&self) -> &HashMap<String, Profesor> {
        &(self.profs)
    }

    //it shouldnt be necessary for this reference to be mutable
    //since these are the reference teacher
    pub fn get_prof(&self, profid: &str) -> &Profesor {
        self.profs.get(profid).unwrap()
    }

    pub fn add_prof(&mut self, prof: Profesor) {
        self.profs.insert(prof.get_id().to_string(), prof);
    }

    pub fn get_clases(&self) -> &HashMap<String, Clase> {
        &(self.clases)
    }

    pub fn get_clase(&self, claseid: &str) -> &Clase {
        self.clases.get(claseid).unwrap()
    }

    pub fn add_clase(&mut self, clase: Clase) {
        self.clases.insert(clase.get_id().to_string(), clase);
    }

    pub fn get_cursos(&self) -> &HashMap<String, Curso> {
        &(self.cursos)
    }

    pub fn get_curso(&self, cursoid: &str) -> &Curso {
        self.cursos.get(cursoid).unwrap()
    }

    pub fn add_curso(&mut self, curso: Curso) {
        self.cursos.insert(curso.get_id().to_string(), curso);
    }


    
}
