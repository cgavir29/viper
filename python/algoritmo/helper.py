import profesor as pr, horario as hr


def copy_prof(prof):
    sch = hr.Horario()
    prof_sch = prof.get_sch(); #schedule for the prof    
    for dia in prof_sch:
        for hora in prof.horario.get_dia(dia):
            sch.diario[dia][hora] = prof.horario.get_horario(dia, hora)
            
    return pr.Profesor(prof.iden, sch, prof.score)


def merge_hashes(hash1, hash2):
    for i in hash2:
        hash1[i] = hash2.get(i)
    return hash1


