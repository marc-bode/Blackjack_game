class Chips:

    def __init__(self, total=100):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self, bet):
        self.bet = bet
        self.total = self.total + self.bet

    def lose_bet(self, bet):
        self.bet = bet
        self.total = self.total - self.bet