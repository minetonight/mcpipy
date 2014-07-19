import random
import time

daljina_pole = 9
broy_igrachi = input("Vavedi broya igrachi <10: ")
pozicii = [0] * broy_igrachi
simvoli_igrachi = ['A', 'I', 'T', 'V', 'O', 'W', 'X', 'Y', 'M', 'H']
tekusht_igrach = 0

while True:
    zar = random.randint(1, 6)
    if pozicii[tekusht_igrach] + zar <= daljina_pole:
        nova_poziciya = pozicii[tekusht_igrach] + zar
        pozicii[tekusht_igrach] = nova_poziciya
        
        sledvasht_igrach = tekusht_igrach + 1
        if sledvasht_igrach == broy_igrachi:
            sledvasht_igrach = 0
           
    for tekushta_poziciya in range(1, daljina_pole + 1):
        simvol_za_izvejdane = '_'
        for index_igrach in range(broy_igrachi):
            if tekushta_poziciya == pozicii[index_igrach]:
                simvol_za_izvejdane = simvoli_igrachi[index_igrach]
        print(simvol_za_izvejdane),

    print(tekusht_igrach)
    if pozicii[tekusht_igrach] >= daljina_pole:
        print ("Specheli igrach: " + simvoli_igrachi[tekusht_igrach])
        break

    tekusht_igrach = sledvasht_igrach 
    time.sleep(2)

