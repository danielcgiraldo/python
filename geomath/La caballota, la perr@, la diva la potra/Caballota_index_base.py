import math





print("Escriba la figura:")
figura=input()
if figura=="cuadrado":
    lado=int(input("lado:"))
    unidad=input("Unidad:")
    print("area:",int(lado*lado),str(unidad),"cuadrados")
    print("perimetro:",int(lado*4),str(unidad))
    print("diagonal:",str(math.sqrt((((lado*lado)+(lado*lado))))),unidad)
elif figura=="triangulo":
    print("¿Quiere saber los ángulos?")
    respuesta=input()
    if respuesta=="si":
        print("cuantos angulos tiene?")
        angulos=int(input())
        if angulos==1:
            print("¿los 2 lados que tiene son correspondientes?")
            correspondiente=input()
            if correspondiente=="si":
                print("coloque los lados y el angulo:")
                lado1=float(input("Lado1: "))
                lado2=float(input("Lado2: "))
                unidad=input("unidad de los lados: ")
                angulo1=math.radians(float(((input("Angulo correspondiente: ")))))
                lado3=(math.sqrt((((lado1*lado1)+(lado2*lado2)))-(2*lado2*lado1*(math.cos(angulo1)))))
                angulo2=math.degrees(math.asin((lado1*math.sin(angulo1))/lado3))
                angulo3=math.degrees(math.asin((lado2*math.sin(angulo1))/lado3))
                angulo1=math.degrees(angulo1)
                print("Lado3: "+str(lado3)+str(unidad))
                print("Lado2: "+str(lado2)+str(unidad))
                print("Lado1: "+str(lado1)+str(unidad))
                print("Angulo1: "+str(angulo1)+"°")
                print("Angulo2: "+str(angulo2)+"°")
                print("Angulo3: "+str(angulo3)+"°")
            if correspondiente=="no":
                print("coloque los lados y el angulo (Teninedo en cuenta que lado_x debe de ser opuesto a angulo_x:")
                lado1=float(input("Lado1: "))
                lado2=float(input("Lado2: "))
                unidad=input("unidad de los lados: ")
                angulo1=(float(((input("Angulo1: ")))))
                angulo3=math.degrees(math.asin((lado2*math.sin(angulo1))/lado1))
                angulo2=180-angulo1-angulo3
                print("Angulo1: "+str(angulo1)+"°")
                print("Angulo2: "+str(angulo2)+"°")
                print("Angulo3: "+str(angulo3)+"°")