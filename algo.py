def logic(p,b,c,m1,m2,l,will):
    pcm,pcb,com,arts,pcmb=0

    t_pcm = 12
    t_pcb = 11.25
    t_pcmb = 14.25
    t_arts = 12
    t_com = 10.5

    # will = 0 : no prefer
    if will == 0:
        pcm += p + c + m1 + (0.5 * m2) + (0.25 * (l + b))
        pcb += p + c + b + (m1 + m2 + l) * 0.25
        pcmb += p + c + b + m1 + (l * 0.25) + (0.5 * m2)
        com += (p + c + m1 + b) * 0.25 + m2 * 2 + l * 0.5
        arts += (p + c + b + m2) * 0.25 + (l + m2) * 1.5

    # will = 1 : arts
    elif will == 1:
        pcm += p + c + m1 + (0.5 * m2) + (0.25 * (l + b))
        pcb += p + c + b + (m1 + m2 + l) * 0.25
        pcmb += p + c + b + m1 + (l * 0.25) + (0.5 * m2)
        com += (p + c + m1 + b) * 0.25 + m2 * 2 + l * 0.5
        arts += (p + c + b + m2) * 0.25 + (l + m2) * 1.5 + 1

    # will = 2 : commerce
    elif will == 2:
        pcm += p + c + m1 + (0.5 * m2) + (0.25 * (l + b))
        pcb += p + c + b + (m1 + m2 + l) * 0.25
        pcmb += p + c + b + m1 + (l * 0.25) + (0.5 * m2)
        com += (p + c + m1 + b) * 0.25 + m2 * 2 + l * 0.5 + 1
        arts += (p + c + b + m2) * 0.25 + (l + m2) * 1.5

    # will = 3 : science
    elif will == 3:
        pcm += p + c + m1 + (0.5 * m2) + (0.25 * (l + b)) + 1
        pcb += p + c + b + (m1 + m2 + l) * 0.25 + 1
        pcmb += p + c + b + m1 + (l * 0.25) + (0.5 * m2) + 1
        com += (p + c + m1 + b) * 0.25 + m2 * 2 + l * 0.5
        arts += (p + c + b + m2) * 0.25 + (l + m2) * 1.5

    per_pcm = (pcm / t_pcm) * 100
    per_pcb = (pcb / t_pcb) * 100
    per_pcmb = (pcmb / t_pcmb) * 100
    per_arts = (arts / t_arts) * 100
    per_com = (com / t_com) * 100
