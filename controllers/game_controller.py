from managers.player_manager import Player
from models.game_model import GameModel
from utils.players import determine_first_attacker


def get_fight_history(json_fight: GameModel):
    player1 = Player(json_fight.player1.movimientos, json_fight.player1.golpes, 'Tonyn')
    player2 = Player(json_fight.player2.movimientos, json_fight.player2.golpes, 'Arnaldor')

    first_attacker, second_attacker = determine_first_attacker(player1, player2)

    result = []

    # Execute fight sequence
    for mov1, strike1, mov2, strike2 in zip(first_attacker.movements, first_attacker.strikes, second_attacker.movements,
                                            second_attacker.strikes):
        if mov1 or strike1:
            move_name, energy_loss = first_attacker.perform_strike(mov1, strike1)
            if mov1:
                result.append({'action': f'{first_attacker.name} realiza el movimiento {mov1}'})
            if strike1:
                result.append({'action': f'{first_attacker.name} ejecuta el golpe {move_name}'})
            second_attacker.set_stamina(energy_loss)
            if second_attacker.stamina == 0:
                result.append({
                    'action': f'{first_attacker.name} Gana la pelea y aun le queda {first_attacker.stamina} de energía'})
                break

        if mov2 or strike2:
            move_name, energy_loss = second_attacker.perform_strike(mov2, strike2)
            if mov2:
                result.append({'action': f'{second_attacker.name} realiza el movimiento {mov2}'})
            if strike2:
                result.append({'action': f'{second_attacker.name} ejecuta el golpe {move_name}'})
            first_attacker.set_stamina(energy_loss)
            if first_attacker.stamina == 0:
                result.append({
                    'action': f'{second_attacker.name} Gana la pelea y aun le queda {second_attacker.stamina} de energía'})
                break

    return result