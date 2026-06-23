class Player:
    def __init__(self, row, col, health=10):
        self.row = row
        self.col = col
        self.has_key = False
        self.health = health
        self.symbol = 'P'

    def take_damage(self, amount=1):
        self.health -= amount

        if self.health < 0:
            self.health = 0

    def heal(self, amount = 1):
        self.health += amount

    def pick_up_key(self):
        self.has_key = True

    def is_alive(self):
        return self.health > 0

    def move_player(self, row, col):
        self.row = row
        self.col = col
