import random
continuar = "s"

while continuar == "s":
    def play():
        usuario = input("Digite 'pi' para piedra, 'p' para papel y 't' para tijera: ")
        computadora = random.choice(['pi', 'p', 't'])

        if usuario == computadora:
            return 'Es un empate'
        if is_win(usuario, computadora):
            return 'Felicidades. Ganaste'
        return 'Lo siento. Perdiste'

    def is_win(jugador, oponente):
        if (jugador == 'pi' and oponente == 't') or (jugador == 'p' and oponente == 't') \
            or (jugador == 't' and oponente == 'p'):
            return True

    print(play())
    continuar = input('¿Quieres continuar (s/n)?: ')