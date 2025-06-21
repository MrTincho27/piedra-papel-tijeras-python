# Lo ingresado por el usuario sea lowercase de tal forma de comparar minuscula con minuscula
# Mas de un turno con el bucle while


nombre1=input("Como se llama el jugador 1?: ")
nombre2=input("Como se llama el jugador 2?: ")
puntaje_jugador_1=0
puntaje_jugador_2=0


juegoterminado=False

while juegoterminado==False:
    print ("RONDA 1")

    jugador1=input("Hola " + nombre1 + " ,que eliges? piedra, papel o tijeras?: ")
    jugador2=input("Hola " + nombre2 + " ,que eliges? piedra, papel o tijeras?: ")

    condicion1= (jugador1=="piedra" and jugador2=="tijeras")
    condicion2= (jugador1=="papel" and jugador2=="piedra") 
    condicion3= (jugador1=="tijeras" and jugador2=="papel")

    if jugador1==jugador2:
        print("Ha sido un empate")
        print("Puntaje Jugador 1", puntaje_jugador_1)
        print("Puntaje Jugador 2", puntaje_jugador_2)


    elif  condicion1 or condicion2 or condicion3:
        print ("Ha ganado ",nombre1)
        puntaje_jugador_1+=1
        print("Puntaje Jugador 1", puntaje_jugador_1)
        print("Puntaje Jugador 2", puntaje_jugador_2)
        
    else: 
        print ("Ha ganado ",nombre2)
        puntaje_jugador_2+=1
        print("Puntaje Jugador 1", puntaje_jugador_1)
        print("Puntaje Jugador 2", puntaje_jugador_2)

    print ("RONDA 2")

    jugador1=input("Hola " + nombre1 + " ,que eliges? piedra, papel o tijeras?: ")
    jugador2=input("Hola " + nombre2 + " ,que eliges? piedra, papel o tijeras?: ")

    condicion1= (jugador1=="piedra" and jugador2=="tijeras")
    condicion2= (jugador1=="papel" and jugador2=="piedra") 
    condicion3= (jugador1=="tijeras" and jugador2=="papel")

    if jugador1==jugador2:
        print("Ha sido un empate")
        print("Puntaje Jugador 1", puntaje_jugador_1)
        print("Puntaje Jugador 2", puntaje_jugador_2)


    elif  condicion1 or condicion2 or condicion3:
        print ("Ha ganado ",nombre1)
        puntaje_jugador_1+=1
        print("Puntaje Jugador 1", puntaje_jugador_1)
        print("Puntaje Jugador 2", puntaje_jugador_2)
        
    else: 
        print ("Ha ganado ",nombre2)
        puntaje_jugador_2+=1
        print("Puntaje Jugador 1", puntaje_jugador_1)
        print("Puntaje Jugador 2", puntaje_jugador_2)

    print ("RONDA 3")

    jugador1=input("Hola " + nombre1 + " ,que eliges? piedra, papel o tijeras?: ")
    jugador2=input("Hola " + nombre2 + " ,que eliges? piedra, papel o tijeras?: ")

    condicion1= (jugador1=="piedra" and jugador2=="tijeras")
    condicion2= (jugador1=="papel" and jugador2=="piedra") 
    condicion3= (jugador1=="tijeras" and jugador2=="papel")

    if jugador1==jugador2:
        print("Ha sido un empate")
        print("Puntaje Jugador 1", puntaje_jugador_1)
        print("Puntaje Jugador 2", puntaje_jugador_2)


    elif  condicion1 or condicion2 or condicion3:
        print ("Ha ganado ",nombre1)
        puntaje_jugador_1+=1
        print("Puntaje Jugador 1", puntaje_jugador_1)
        print("Puntaje Jugador 2", puntaje_jugador_2)
        
    else: 
        print ("Ha ganado ",nombre2)
        puntaje_jugador_2+=1
        print("Puntaje Jugador 1", puntaje_jugador_1)
        print("Puntaje Jugador 2", puntaje_jugador_2)


    print("Resultados finales")
    print(nombre1,puntaje_jugador_1)
    print(nombre2,puntaje_jugador_2)

    if puntaje_jugador_1>puntaje_jugador_2:
        print("Ha ganado " + nombre1)
    elif puntaje_jugador_1<puntaje_jugador_2:
        print ("Ha ganado " + nombre2)
    else:
        print ("Ha sido un empate")

    break

