def take_bet(chips):
    while True:
        try:
            bet = int(input('Enter an amount to bet this game. Your current balance is {} chips: '.format(chips)))
        except:
            print('Please enter a positive integer value for your bet!')
        else:
            break
    return bet

def hit(deck,hand,values):
    hit_card = deck.deal()
    hand.add_card(hit_card,values)


def hit_or_stand(deck,hand,values):
    global playing  # to control an upcoming while loop
    decision = input('Would you like to hit or stand? ')
    if decision.lower() == 'hit':
        hit(deck,hand,values)
        return True
    else:
        return False


def show_some(player, dealer):
    player_hand = ''
    dealer_hand = ''
    for card in player.cards:
        player_hand += card.__str__() + ', '  # add each Card object's print string
    dealer_hand = dealer.cards[0].__str__()
    print('Player hand is: {}'.format(player_hand))
    print('Dealer hand is: {}'.format(dealer_hand))


def show_all(player, dealer):
    player_hand = ''
    dealer_hand = ''
    for card in player.cards:
        player_hand += card.__str__() + ', '  # add each Card object's print string
    for card in dealer.cards:
        dealer_hand += card.__str__() + ', '
    print('Player hand is {}'.format(player_hand))
    print('Dealer hand is {}'.format(dealer_hand))


def player_busts(bet, player_chips):
    print('You bust!')
    player_chips.lose_bet(bet)


def player_wins(bet, player_chips):
    print('You win!')
    player_chips.win_bet(bet)


def dealer_busts(bet, player_chips):
    print('Dealer busts, you win!')
    player_chips.win_bet(bet)


def dealer_wins(bet, player_chips):
    print('Dealer beat your hand, you lose!')
    player_chips.lose_bet(bet)


def push():
    print('Draw!')