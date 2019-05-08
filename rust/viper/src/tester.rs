use crate::{
    clase::Clase, curso::Curso, escuela::Escuela, horario::Horario, profesor::Profesor,
    simdata::create_rnd_esc, solucion::Solucion, lns::test_lns
};

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

    let mut hr2 = Horario::new();
    let horas = vec![6, 7, 8];
    let val = "hello2";
    hr2.set_horario("l", &horas, val, true);
    hr2.set_horario("m", &horas, "043", true);
    hr2.set_single("w", 16, "goodbye2");

    println!("equal? {}", hr1.equal_to(&hr2));

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
    let mut esc1 = Escuela::new("test".to_string());

    let mut crs1 = Curso::new("1".to_string());
    crs1.add_reqr("eng a1");
    esc1.add_curso(crs1);

    let prof1 = Profesor::new("pr1".to_string());

    let mut prof2 = Profesor::new("pr2".to_string());
    prof2.set_vars("simevi", 5);
    prof2.add_reqr("eng a1");
    prof2.add_sede("p");
    prof2.set_avail(&vec!["l".to_string()], &vec![6, 7, 8, 9]);

    let mut this_id = String::from(esc1.get_curso("1").get_id());
    this_id.push_str("1");
    let mut clase1 = Clase::new(this_id, "1", "p");

    clase1.set_horario(&vec!["l"], &vec![6, 7, 8, 9]);
    clase1.add_cand(&prof1);
    clase1.add_cand(&prof2);

    assert_eq!(clase1.can_teach(&prof2, &esc1), true);

    println!("cands {:?}", clase1.get_cands());
    println!("class name {}", clase1.get_id());
    println!("venue {}", clase1.get_sede());
    println!("sch \n{}", clase1.get_horario());
    println!("{}", clase1.get_prof());

    test2_clase(&clase1);
}

fn test2_clase(clase: &Clase) -> &Horario {
    println!("test2 {}", clase.get_id());
    clase.get_horario()
}

fn test_profesor() {
    let mut prof1 = Profesor::new("arnoldo".to_string());
    prof1.add_reqr("hello");
    prof1.set_avail(
        &vec!["l".to_string(), "m".to_string()],
        &vec![13, 14, 15, 16],
    );
    let mut sch1 = Horario::new();
    sch1.set_horario("l", &vec![14, 15], "34", true);
    println!(" IS AVAIL {}", prof1.is_avail(&sch1));
    // println!("{}", prof1.get_horario());

    let mut hr1 = Horario::new();
    let horas = vec![6, 7, 8];
    let val = "hello";
    hr1.set_horario("l", &horas, val, true);
    hr1.set_horario("m", &horas, "0", true);
    hr1.set_single("w", 16, "goodbye");
    prof1.add_sede("p");
    prof1.copy_avail_sch(&hr1);

    let mut clase1 = Clase::new("hello".to_string(), "1", "p");
    clase1.set_horario(&vec!["l"], &vec![6, 7, 8]);
    println!(" IS AVAIL {}", prof1.is_avail(clase1.get_horario()));

    println!("{}", prof1.get_horario());
    println!("\n {}", clase1.get_horario());

    prof1.add_clase(&clase1);
    println!(" IS AVAIL {}", prof1.is_avail(clase1.get_horario()));
    println!("{}", prof1.get_horario());
}

fn test_escuela() {
    let mut esc1 = create_rnd_esc(
        300,
        0.75,
        1.0,
        0.3,
        &vec![
            "simevi",
            "microteaching",
            "promedio_eval",
            "pdp_cum",
            "estatus",
        ],
        &vec!["u", "s", "l", "b", "r", "p"],
    );

    println!("cursos {}", esc1.get_cursos().keys().len());
    println!("clases {}", esc1.get_clases().keys().len());
    println!("profes {}", esc1.get_profs().keys().len());

    let mut num_empty_classes = 0;
    let mut avg_num_cands = 0;
    for (_, clase) in esc1.get_clases() {
        // println!("{}", clase.get_cands().len());
        if clase.get_cands().len() == 0 {
            num_empty_classes += 1;
        }
        avg_num_cands += clase.get_cands().len();
    }
    println!("num classes with no takers: {}", num_empty_classes);
    println!(
        "avg num of cands per class: {}",
        avg_num_cands / esc1.get_clases().len()
    );
}

fn test_sol() {
    let mut esc1 = create_rnd_esc(
        400,
        0.75,
        1.0,
        0.8,
        &vec![
            "simevi",
            "microteaching",
            "promedio_eval",
            "pdp_cum",
            "estatus",
        ],
        &vec!["u", "s", "l", "b", "r", "p"],
    );
    let mut sol1 = Solucion::new();

    for (_, clase) in esc1.get_clases() {
        let prof_id = &clase.get_cands().get(0).unwrap().0;
        // println!("{}", prof_id);
        let prof_ref = esc1.get_prof(prof_id);
        sol1.add_prof(prof_ref);
    }

    let test_clase = esc1.get_clase("359l6");

    let profid1 = &test_clase.get_cands().get(0).unwrap().0;

    sol1.set_clprof(test_clase, profid1);
    println!("{:?}", sol1.get_clprof("359l6"));

    println!(
        "{}, {}",
        sol1.get_profs().get(profid1).unwrap().0,
        sol1.get_profs().get(profid1).unwrap().1
    );
    println!("active profs {}", sol1.get_actprofs());
    println!("score {}", sol1.get_score());

    let profid2 = &test_clase.get_cands().get(1).unwrap().0;
    sol1.set_clprof(test_clase, profid2);

    println!("{:?}", sol1.get_clprof("359l6"));
    println!(
        "{}, {}",
        sol1.get_profs().get(profid1).unwrap().0,
        sol1.get_profs().get(profid1).unwrap().1
    );

    println!(
        "{}, {}",
        sol1.get_profs().get(profid2).unwrap().0,
        sol1.get_profs().get(profid2).unwrap().1
    );
    println!("active profs {}", sol1.get_actprofs());
    println!("score {}", sol1.get_score());

    let mut sol3 = Solucion::new();
    
    
}

pub fn test_main() {
    println!("--------------------------testing horario");
    test_horario();
    println!("\n--------------------------testing curso");
    test_curso();
    println!("\n--------------------------testing clase");
    test_clase();
    println!("\n-----------------------testing profesor");
    test_profesor();
    println!("\n------------------------testing escuela");
    test_escuela();
    println!("\n-----------------------testing solucion");
    // test_sol();
    println!("\n----------------------------testing lns");
    test_lns();
    
}
