use crate::{
    clase::Clase, curso::Curso, escuela::Escuela, horario::Horario, profesor::Profesor,
    simdata::create_rnd_esc, solucion::Solucion,
};
use std::cmp::Ordering;

fn sort_keys<'a>(clases_index: &mut Vec<&'a str>) {
    
    let temp_fn = |a: &str, b: &str| -> Ordering {
        
        if a.get_score() > b.get_score() {
            Ordering::Greater
        } else {
            Ordering::Less
        }
    };


    
    clases_index.sort_by(temp_fn);
}

pub fn do_lns() {
    println!("REMEMBER TO SORT CANDIDATES, CURRENTLY DORTING IN SIMDATA");
}
