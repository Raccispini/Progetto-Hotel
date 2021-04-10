from Sezione import Sezione
sections = []
menu = ['1)Aggiungi\t\t\t\t|','2)Modifica\t\t\t\t|','3)Elimina\t\t\t\t|','0)Esci\t\t\t\t\t|']
def print_menu(menu,sections):
    if len(sections) < len(menu):
        for i in range(len(sections)):
            print(menu[i]+' ' +str(i+1)+' - '+sections[i])
        for i in range(len(sections),len(menu)):
            print(menu[i])
    else:
        for i in range(len(menu)):
            print(menu[i]+' '+str(i+1)+' - '+sections[i])
        for i in range(len(menu),len(sections)):
            print('\t\t\t\t\t| '+ str(i+1)+' - '+sections[i])

#Menu
while True:
    print("Menu:\t\t\t\t\t| Lista sezioni': ")
    nomi = []
    for i in range(len(sections)):
        nomi.append(sections[i].nome)

    print_menu(menu,nomi)
     
    scelta = int(input())
    
    if scelta == 1:
        print("Aggiungi")
        nome = input('Inserisci il nome della sezione : ')
        sections.append(Sezione(nome))
    if scelta == 2:
        print('Modifica')
        while True:
           n = int(input('Scegli la sezione da modificare :'))
           n-=1
           if n < len(sections)+1 and n>0:
               break
        while True:
            print('Menu sezione : '+sections[n].nome)
            nomi = []
            if len(sections[n].attivita)>0:
                for i in range(len(sections[i].attivita)):
                    nomi.append(sections[i].attivita[i].nome)
            print_menu(['1)Aggiungi attivita','2)Modifica attivita','3)Elimina attivita','0)Torna al menu'],nomi)
            scelta = int(input())

            if scelta == 1:
                print('Aggiungi attivita')
            if scelta == 2:
                print('Modifica attivita')
            if scelta == 3:
                print('Elimina attivita')
            if scelta == 0:
                break

    if scelta == 3:
        print('Elimina')
    if scelta == 0:
        break