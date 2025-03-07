import random
import time
player1_vida = int(input("Ingresa la vida del primer jugador: "))
player2_vida = int(input("Ingresa la vida del segundo jugador: "))
turno = 0
regenerar = False

while player1_vida > 0 and player2_vida > 0:
    turno += 1
    print(f"\nTurno N°: {turno}")
    #Jugador uno ataca


    #Esto es que el jugador 2 tiene un 20% de esquivar el ataque, y random.random me devuelve un flotante entre 0 y uno
    if regenerar:
        print("El jugador 1 se esta regenerando de la patada. No puede atacar")
        regenerar = False    
    elif random.random() > 0.20:    
        jugador1_ataque = random.randint(10, 100)
        print(f"El jugador 1 ataca con un golpe de {jugador1_ataque} de daño")
        if jugador1_ataque == 100:
            print("El jugador 1 acierta un golpe critico. Vuelve a pegar pq el 2 tiene que regenerarse")
            regenerar = True

        player2_vida -= jugador1_ataque
        if player2_vida <= 0:
            print("El jugador 2 no aguanto los golpes de el jugador 1")
            break
        else:
            print(f"Vida restante del jugador 2: {player2_vida}")
    else:
        print("El jugador 2 esquivo el ataque del jugador 1.")


    #Jugador dos ataca

    #Esto es que el jugador 1 tiene un 25% de esquivar el ataque, y random.random me devuelve un flotante entre 0 y uno
    if regenerar:
        print("El jugador 2 se esta regenerando del golpe. No puede atacar")
        regenerar = False
    elif random.random() > 0.25:    
        jugador2_ataque = random.randint(10, 120)
        print(f"El jugador 2 ataca con una patada de {jugador2_ataque} de daño")
        if jugador2_ataque == 120:
            print("El jugador 2 acierta un golpe critico. Vuelve a pegar pq el 1 tiene que regenerarse")
            regenerar = True

        player1_vida -= jugador2_ataque
        if player1_vida <= 0:
            print("El jugador 1 no aguanto las patadas de el jugador 2")
            break
        else:
            print(f"Vida restante del jugador 1: {player1_vida}")
    else:
        print("El jugador 1 esquivo el ataque del jugador 2.")

    time.sleep(1.5)



if player1_vida > 0:
    print("El jugador 1 gana la partida")
else:
    print("El jugador 2 gana la partida")