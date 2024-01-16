class Player:
    def __init__(self, movements, strikes, name):
        self.name = name
        self.stamina = 6
        self.movements = movements
        self.strikes = strikes

    def set_stamina(self, energy_loss):
        self.stamina = max(0, self.stamina - energy_loss)

    def perform_move(self, movement):
        return f'{self.name} realiza el movimiento {movement}'

    def perform_strike(self, movement, strike):
        move_name, energy_loss = self.get_special_move(movement, strike)
        return move_name, energy_loss

    def get_special_move(self, movement, strike):
        # Combinaciones para Tonyn Stallone
        if self.name == 'Tonyn':
            if movement == 'DSD' and strike == 'P':
                return 'Taladoken', 3
            elif movement == 'SD' and strike == 'K':
                return 'Remuyuken', 2

        # Combinaciones para Arnaldor Shuatseneguer
        elif self.name == 'Arnaldor':
            if movement == 'SA' and strike == 'K':
                return 'Remuyuken', 3
            elif movement == 'ASA' and strike == 'P':
                return 'Taladoken', 2

        # Movimientos normales
        if strike in ['P', 'K']:
            return 'Puño o Patada', 1
        return '', 0