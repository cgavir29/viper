use crate::{clase::Clase, curso::Curso, escuela::Escuela, horario::Horario, profesor::Profesor, solucion::Solucion};

fn test_horario() -> Horario {
    let mut hr1 = Horario::new();
    let horas = vec![6, 7, 8];
    let val = "hello";
    hr1.set_horario("l", &horas, val, true);
    hr1.set_horario("m", &horas, "0", true);
    hr1.set_single("w", 16, "goodbye");
    println!("{}", hr1.count_avail() == 3);
    println!("{}", hr1);
    println!("{:?}", hr1.get_dia("l"));
    hr1
}

fn test_curso() -> Curso {
    let mut crs1 = Curso::new(String::from("engal1"));
    crs1.add_reqr("engal1");
    println!("{}", crs1);
    println!("{:?}", crs1.get_reqr());
    println!("{:?}", crs1.get_reqr());
    println!("{}", crs1.get_id());
    println!("{}", crs1.get_id());
    crs1
}

fn test_clase() {

    
    let mut crs1 = Curso::new("engal1".to_string());
    crs1.add_reqr("eng a1");
    
    let prof1 = Profesor::new("pr1".to_string());
    let mut prof2 = Profesor::new("pr2".to_string());
    prof2.set_vars("simevi", 5);
    prof2.add_reqr("eng a1");
    prof2.add_sede("p");
    prof2.set_avail(&vec!["l".to_string()], &vec![6, 7, 8, 9]);
    
    let mut this_id = String::from(crs1.get_id());
    this_id.push_str("1");
    let mut clase1 = Clase::new(this_id, &crs1, "p");

    clase1.set_horario(&vec!["l".to_string()], &vec![6, 7, 8, 9]);
    clase1.add_cand(&prof1);
    clase1.add_cand(&prof2);

    assert_eq!(clase1.can_teach(&prof2), true);
    
    println!("cands {:?}", clase1.get_cands());
    println!("class name {}", clase1.get_id());
    println!("venue {}", clase1.get_sede());
    println!("sch \n{}", clase1.get_horario());
    println!("{}", clase1.get_prof());

    test2_clase(&clase1);
}


fn test2_clase<'a>(clase: &'a Clase) -> &'a Horario{
    println!("test2 {}", clase.get_id());
    clase.get_horario()
}

fn test_profesor() {
    let mut prof1 = Profesor::new("arnoldo".to_string());
    prof1.add_reqr("hello");
    prof1.set_avail(&vec!["l", "m"], &vec![13,14,15,16]);
    let mut sch1 = Horario::new();
    sch.set_horario("l", &vec![14,15], "0", true);
    println!("{}",prof1.is_avail(&sch1));
    let hor1: &Horario = prof1.get_sch();

    
    
    


}


pub fn test_main() {
    println!("--------------------------testing horario");
    test_horario();
    println!("\n--------------------------testing curso");
    test_curso();
    println!("\n--------------------------testing clase");
    test_clase();
}
