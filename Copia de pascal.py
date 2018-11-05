def main():    
    nivel=int(input("introducir el nivel del tringulo de pascal"))
    pascal(nivel)

def pascal(nivel):
    if nivel==1:
        print([1])
    if nivel==2:
        print([1])
        print([1,1])
    if nivel==3:
        print([1])
        print([1,1])
        print([1,2,1])
    if nivel>3:
        nlinea=[]
        print([1])
        print([1,1])
        linea=[1,2,1]
        print(linea)
        x=2
        while x<=nivel-2:
            nlinea=[]
            y=1
            nlinea.append(1)
            nlinea.append(linea[1]+1)
            while y<x:
                nlinea.append(linea[y]+linea[y+1])
                y+=1
            nlinea.append(1)
            x+=1
            print(nlinea)
            linea=nlinea
main()            
