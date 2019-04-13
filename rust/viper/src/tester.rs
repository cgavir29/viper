use crate::horario::Horario;
use crate::curso::Curso;
use crate::clase::Clase;

fn test_horario() -> Horario{
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
    let hr1 = Horario::new();
    let crs1 = Curso::new("engal1".to_string());
    let mut this_id = String::from(crs1.get_id());
    this_id.push_str("1");
    let mut clase1 = Clase::new(this_id, crs1.get_id(), "p");

    clase1.set_horario(&vec!["l".to_string()], &vec![6,7,8,9]);
    println!("{}", clase1.get_id());
    println!("{}", clase1.get_sede());
    println!("{}", clase1.get_horario());
    println!("{}", clase1.get_prof());
    
      


}


pub fn test_main() {
    println!("--------------------------testing horario");
    test_horario();
    println!("\n--------------------------testing curso");    
    test_curso(); 
    println!("\n--------------------------testing clase");
    test_clase();
}
