import math
listafigura=["cuadrado","triangulo","rectangulo","circulo","ovalo","trapecio","rombo"]
listasino=["si","no"]
listaangulos=[1,2,3]

print("Escriba la figura:"+str(listafigura))
figura=input()
if figura=="cuadrado":
    lado=int(input("lado:"))
    unidad=input("Unidad:")
    print("area:",int(lado*lado),str(unidad),"cuadrados")
    print("perimetro:",int(lado*4),str(unidad))
    print("diagonal:",str(math.sqrt((((lado*lado)+(lado*lado))))),unidad)
elif figura=="triangulo":
    print("¿Quiere saber los ángulos?"+str(listasino))
    respuesta=input()
    if respuesta=="si":
        print("cuantos angulos tiene?"+str(listaangulos))
        angulos=int(input())
        if angulos==1:
            print("¿los 2 lados que tiene son correspondientes?"+str(listasino))
            correspondiente=input()
            if correspondiente=="si":
                print("coloque los lados y el angulo:")
                lado1=float(input("Lado1: "))
                lado2=float(input("Lado2: "))
                unidad=input("unidad de los lados: ")
                angulo3=math.radians(float(((input("Angulo correspondiente: ")))))
                lado3=(math.sqrt((((lado1*lado1)+(lado2*lado2)))-(2*lado2*lado1*(math.cos(angulo3)))))
                angulo2=math.degrees(math.asin((lado1*math.sin(angulo3))/lado3))
                angulo1=math.degrees(math.asin((lado2*math.sin(angulo3))/lado3))
                area=lado1*lado2*math.sin(angulo3)
                angulo3=math.degrees(angulo3)
                print("----------RESULTADOS----------")
                print("Lado3: "+str(lado3)+str(unidad))
                print("Lado2: "+str(lado2)+str(unidad))
                print("Lado1: "+str(lado1)+str(unidad))
                print("perimetro: "+str(lado1+lado2+lado3)+unidad)
                print("Area: "+str(area)+str(unidad)+"²")
                print("Angulo1: "+str(angulo1)+"°")
                print("Angulo2: "+str(angulo2)+"°")
                print("Angulo3: "+str(angulo3)+"°")
                print("Suma de angulos: "+str(angulo1+angulo2+angulo3))
                print("----------FIN DE RESULTADO----------")
            if correspondiente=="no":
                print("coloque los lados y el angulo (Teninedo en cuenta que lado_x debe de ser opuesto a angulo_x:")
                lado1=float(input("Lado1: "))
                lado2=float(input("Lado2: "))
                unidad=input("unidad de los lados: ")
                angulo1=math.radians((float(((input("Angulo1: "))))))
                angulo2=math.degrees(math.asin(((lado2*math.sin(angulo1))/lado1)))
                angulo1=math.degrees(angulo1)
                angulo3=math.radians(180.0-angulo1-angulo2)
                lado3=(math.sqrt((((lado1*lado1)+(lado2*lado2)))-(2*lado2*lado1*(math.cos(angulo3)))))
                area=lado1*lado2*math.sin(angulo3)
                angulo3=math.degrees(angulo3)
                print("----------RESULTADOS----------")
                print("Lado3: "+str(lado3)+str(unidad))
                print("Lado2: "+str(lado2)+str(unidad))
                print("Lado1: "+str(lado1)+str(unidad))
                print("perimetro: "+str(lado1+lado2+lado3)+unidad)
                print("Area: "+str(area)+str(unidad)+"²")
                print("Angulo1: "+str(angulo1)+"°")
                print("Angulo2: "+str(angulo2)+"°")
                print("Angulo3: "+str(angulo3)+"°")
                print("Suma de angulos: "+str(angulo1+angulo2+angulo3))
                print("----------FIN DE RESULTADO----------")
        elif angulos==2:
            print("cuantos lados conoce?")
        elif angulos==3:
            print("Ya se conocen todos los angulos")
        else:
            print("No se ha detectado la cantidad de angulos")
elif figura=="rectangulo":
    print("inserte el valor de la base yla altura")
elif figura=="circulo":
    print=("conoce el radio?")
elif figura=="ovalo":
    print("inserte el valor de los dos radios")
elif figura=="trapecio":
    print("conoce las dos bases?")
elif figura=="rombo":
    print("inserte el valor de ambos lados")
else:
    print("No se ha detectado la figura")
    print("----------FIN DE LA LECTURA----------")