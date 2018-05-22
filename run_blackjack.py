
from Chips import Chips
from Deck import Deck
from Hand import Hand
from blackjack_functions import take_bet,show_all,show_some,hit,hit_or_stand,player_busts,player_wins,push
from blackjack_functions import dealer_busts,dealer_wins

suits = suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

print('Welcome to blackjack!')
deck = Deck(suits,ranks)
deck.shuffle()
player_chips = Chips()
Play = True
while Play == True:

    player = Hand()
    dealer = Hand()
    if player_chips.total == 0:
        print('Sorry, you have lost all your chips. Please come back later.')
        break
    bet = take_bet(player_chips.total)
    playing = True
    if player_chips.total < bet:
        print('Insufficient chips, please make a lower bet. Your chip balance is {}'.format(player_chips.total))
        bet = take_bet()
    player.add_card(deck.deal(),values)
    player.add_card(deck.deal(),values)
    dealer.add_card(deck.deal(),values)
    dealer.add_card(deck.deal(),values)
#    show_some(player, dealer)

    while playing:
        show_some(player, dealer)
        playing = hit_or_stand(deck, player, values)

        if player.aces != 0:
            while True:
                try:
                    ace_decision = input('Would you like to adjust your ace? (y/n) ')
                except:
                    print('Please enter a valid response.')
                    continue
                if ace_decision == 'y' or ace_decision == 'n':
                    break

            if ace_decision == 'y':
                player.adjust_for_ace()
            elif ace_decision == 'n':
                pass

        if player.value > 21:
            player_busts(bet, player_chips)
            print('Your chips balance is {}'.format(player_chips.total))
            while True:
                try:
                    play = input('Would you like to play again? (y/n) ')
                except:
                    print('Please enter a valid response.')
                    continue
                if play == 'y' or play == 'n':
                    break
            if play == 'y':
                break
            elif play == 'n':
                Play = False
            break

    if player.value < 22:
        while dealer.value < 17:
            hit(deck, dealer, values)
        print('Dealer is hitting...')
        show_all(player, dealer)
        if player.value > dealer.value:
            player_wins(bet, player_chips)
        if dealer.value > 21:
            dealer_busts(bet, player_chips)
        if (dealer.value > player.value) & (dealer.value < 22):
            dealer_wins(bet, player_chips)
        if dealer.value == player.value:
            push()
        print('Your chip balance is {}'.format(player_chips.total))
        while True:
            try:
                play = input('Would you like to play again? (y/n) ')
            except:
                print('Please enter a valid response.')
                continue
            if play == 'y' or play == 'n':
                break
        if play == 'y':
            continue
        elif play == 'n':
            Play = False