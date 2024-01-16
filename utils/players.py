def determine_first_attacker(player1, player2):
    # Contar botones (movimientos + golpes) para cada jugador
    p1_button_count = sum(len(mov) + 1 for mov in player1.movements if mov) + len(player1.strikes)
    p2_button_count = sum(len(mov) + 1 for mov in player2.movements if mov) + len(player2.strikes)

    # Comparar cantidad de botones, luego movimientos, luego golpes
    if p1_button_count < p2_button_count:
        return player1, player2
    elif p1_button_count > p2_button_count:
        return player2, player1
    else:
        # En caso de empate, comprobar movimientos y luego golpes
        if len(player1.movements) < len(player2.movements):
            return player1, player2
        elif len(player1.movements) > len(player2.movements):
            return player2, player1
        else:
            if len(player1.strikes) <= len(player2.strikes):
                return player1, player2
            else:
                return player2, player1