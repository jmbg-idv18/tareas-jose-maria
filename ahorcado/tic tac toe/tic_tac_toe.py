import random

def main():
    gm=int(input("introducir 1 para jugar player vs player o 2 para player vs cpu"))
    if gm==1:
        pvp()
    if gm==2:
        pvc()

def win(winer,l1,l2,l3):
    if (l1[0]=="x" and l1[1]=="x" and l1[2]=="x") or (l2[0]=="x" and l2[1]=="x" and l2[2]=="x") or (l3[0]=="x" and l3[1]=="x" and l3[2]=="x") or (l1[0]=="x" and l2[0]=="x" and l3[0]=="x") or (l1[1]=="x" and l2[1]=="x" and l3[1]=="x") or (l1[2]=="x" and l2[2]=="x" and l3[2]=="x") or (l1[0]=="x" and l2[1]=="x" and l3[2]=="x") or (l1[2]=="x" and l2[1]=="x" and l3[0]=="x"):
        winer="x"

    if (l1[0]=="o" and l1[1]=="o" and l1[2]=="o") or (l2[0]=="o" and l2[1]=="o" and l2[2]=="o") or (l3[0]=="o" and l3[1]=="o" and l3[2]=="o") or (l1[0]=="o" and l2[0]=="o" and l3[0]=="o") or (l1[1]=="o" and l2[1]=="o" and l3[1]=="o") or (l1[2]=="o" and l2[2]=="o" and l3[2]=="o") or (l1[0]=="o" and l2[1]=="o" and l3[2]=="o") or (l1[2]=="o" and l2[1]=="o" and l3[0]=="o"):
        winer="o"

    if (l1[0]!=" " and l1[1]!=" " and l1[2]!=" ") and (l2[0]!=" " and l2[1]!=" " and l2[2]!=" ") and (l3[0]!=" " and l3[1]!=" " and l3[2]!=" ") and winer!="x" and winer!="o":
        winer="empate"
    if (winer==" "):
       winer=" "
    return winer

def pvp():
    l1=["1a","1b","1c"]
    l2=["2a","2b","2c"]
    l3=["3a","3b","3c"]
    l1l=[" "," "," "]
    l2l=[" "," "," "]
    l3l=[" "," "," "]
    movdis=["1a","2a","3a","1b","2b","3b","1c","2c","3c"]
    winer=" "
    x=random.randint(0,10)
    if x%2==0:
        turnox=True
    if x%2!=0:
        turnox=False
    while winer==" ":
        print(l1)
        print(l2)
        print(l3)
        if turnox==True:
            print("turno de p1(x)")
        if turnox==False:
            print("turno de p2(o)")
        move=str(input("introducir un movimiento válido(ej:1a)"))
        move=move.lower()
        if move in movdis:
            if move in l1:
                movdis.remove(move)
            if move in l2:
                movdis.remove(move)
            if move in l3:
                movdis.remove(move)
            y=0
            for x in l1:
                if x==move:
                    if turnox==True:
                        l1l[y]="x"
                    else:
                        l1l[y]="o"
                y+=1
            y=0
            for x in l2:
                if x==move:
                    if turnox==True:
                        l2l[y]="x"
                    else:
                        l2l[y]="o"
                y+=1
            y=0
            for x in l3:
                if x==move:
                    if turnox==True:
                        l3l[y]="x"
                    else:
                        l3l[y]="o"
                y+=1
            print(l1l)
            print(l2l)
            print(l3l)
            print("\n")
            turnox=not turnox
            winer=win(winer,l1l,l2l,l3l)
        else:
            print("la casilla "+move+" no es válida o está ocupada")
            print(l1l)
            print(l2l)
            print(l3l)
            print("\n")
    if winer=="x":
        print("ha ganado p1")
        with open("registro.txt", "a") as myfile:
            myfile.write("gana p1 a p2\n")
    if winer=="o":
        print("ha ganado p2")
        with open("registro.txt", "a") as myfile:
            myfile.write("gana p2 a p1\n")
    if winer=="empate":
        print("empate")
        with open("registro.txt", "a") as myfile:
            myfile.write("empatan p1 y p2\n")

def pvc():
    l1=["1a","1b","1c"]
    l2=["2a","2b","2c"]
    l3=["3a","3b","3c"]
    l1l=[" "," "," "]
    l2l=[" "," "," "]
    l3l=[" "," "," "]
    movdis=["1a","2a","3a","1b","2b","3b","1c","2c","3c"]
    winer=" "
    x=random.randint(1,2)
    if x==1:
        turnox=True
    else:
        turnox=False
    while winer==" ":
        print(l1)
        print(l2)
        print(l3)
        if turnox==True:
            print("turno de p1(x)")
        else:
            print("turno de cpu(o)")
        if turnox==True:
            move=str(input("introducir un movimiento válido(ej:1a)"))
        else:
            m=-1
            for x in movdis:
                m+=1
            move=movdis[random.randint(0,m)]
        move=move.lower()
        if move in movdis:
            if move in l1:
                movdis.remove(move)
            if move in l2:
                movdis.remove(move)
            if move in l3:
                movdis.remove(move)
            y=0
            for x in l1:
                if x==move:
                    if turnox==True:
                        l1l[y]="x"
                    else:
                        l1l[y]="o"
                y+=1
            y=0
            for x in l2:
                if x==move:
                    if turnox==True:
                        l2l[y]="x"
                    else:
                        l2l[y]="o"
                y+=1
            y=0
            for x in l3:
                if x==move:
                    if turnox==True:
                        l3l[y]="x"
                    else:
                        l3l[y]="o"
                y+=1
            print(l1l)
            print(l2l)
            print(l3l)
            print("\n")
            turnox=not turnox
            winer=win(winer,l1l,l2l,l3l)
        else:
            print("la casilla "+move+" no es válida o está ocupada")
            print(l1l)
            print(l2l)
            print(l3l)
            print("\n")
    if winer=="x":
        print("ha ganado p1")
        with open("registro.txt", "a") as myfile:
            myfile.write("gana p1 a cpu\n")
    if winer=="o":
        print("ha ganado cpu")
        with open("registro.txt", "a") as myfile:
            myfile.write("gana cpu a p1\n")
    if winer=="empate":
        print("empate")
        with open("registro.txt", "a") as myfile:
            myfile.write("empatan p1 y cpu\n")
I=1
while I==1:
    I=int(input("iniciar el juego(1), quitar el juego(2)(introducir número)"))
    if I==1:
        main()