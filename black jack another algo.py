
import random
import time


class Game():

    def __init__(self):
        self.suits = ["HEARTS" , "SPADES" , "DIAMONDS" , "CLUBS"]
        self.card_rank = {"A":11 , "2":2 , "3":3 , "4":4 , "5":5 , "6":6 , "7":7 , "8":8 , "9":9 , "10":10 , "J":10 , "Q":10 , "K":10}

        self.deck = []

        self.dealer_card = []
        self.player_card = []

        self.total_value_dealer = []
        self.total_value_player = []

        self.current_money = 0
        self.bet = 0

        self.hit = True


    def build_deck(self):
        for suit in self.suits:
            for card , value in self.card_rank.items():
                generat_cards = [card , value , suit]
                self.deck.append(generat_cards)

        random.shuffle(self.deck)


    def get_money(self):
        print("The minimum bet at this table is $20.")
        self.current_money = int(input("how much money are you willing to play with today: "))
        while self.current_money < 20:
            self.current_money = int(input("how much money are you willing to play with today: "))

        self.bet = int(input("what would you like to bet (minimum bet of): "))
        while self.bet < 20 or self.bet > self.current_money:
            self.bet = int(input("what would you like to bet (minimum bet of): "))



    def draw_money(self):
        print("\nCurrent Money: " + str(self.current_money))
        print("Current Bet: " + str(self.bet))



    def distribution_cards_to_dealer_and_player(self):
        for i in range(2):
            random_card = random.choices(self.deck)
            self.dealer_card.append(random_card[0])
            self.total_value_dealer.append(random_card[0][1])
            self.deck.remove(random_card[0])

            random_card = random.choices(self.deck)
            self.player_card.append(random_card[0])
            self.total_value_player.append(random_card[0][1])
            self.deck.remove(random_card[0])



    def draw_dealer_face_up_card(self):
        print("\nDealer is showing " + self.dealer_card[0][0]  + " of " + self.dealer_card[0][2])



    def draw_dealer_hand(self):
        print("\nDealer is set with a total of " + str(len(self.dealer_card)) + " cards.")
        input("\nPress enter to reveal the dealer's cards.")
        for cards in self.dealer_card:
            time.sleep(0.5)
            print(cards[0] + " of " + cards[2])
        

    def draw_player_hand(self):
        print("\nplayer hand")
        for cards in self.player_card:
            time.sleep(0.5)
            print(cards[0] + " of " + cards[2])
        print("total value : " + str(sum(self.total_value_player)))



    def player_hit(self):
        random_card = random.choices(self.deck)
        self.player_card.append(random_card[0])
        self.total_value_player.append(random_card[0][1])
        self.deck.remove(random_card[0])
        self.hit = False


                

    def dealer_hit(self):
        value = sum(self.total_value_dealer)
        while value < 17:
            random_card = random.choices(self.deck)
            self.dealer_card.append(random_card[0])
            value += random_card[0][1]
            self.deck.remove(random_card[0])
        self.total_value_dealer = value



    def check_if_winner(self):
        p_value = sum(self.total_value_player)
        d_value = self.total_value_dealer
        if p_value > 21:
            print("youe went over 21......you loose!!")
            self.current_money -= self.bet

        elif d_value > 21:
            print("Dealer went over 21.....you win!!")
            self.current_money += self.bet

        elif p_value == 21:
            print("you get 21......you win!!")
            self.current_money += self.bet

        elif d_value == 21:
            print("Dealer get 21......you looose!!")
            self.current_money -= self.bet

        elif p_value == d_value:
            print("it's bush")

        elif self.hit == False and p_value < 21 and d_value < 21:
            if p_value > d_value:
                print("you are closer to 21....you win!!")
                self.current_money += self.bet
            elif d_value > p_value:
                print("Dealer are closer to 21......you loose!!")
                self.current_money -= self.bet
                


black_jack = Game()

black_jack.get_money()
running = True
while running:

    black_jack.draw_money()
    
    black_jack.build_deck()

    
    black_jack.distribution_cards_to_dealer_and_player()
    
    black_jack.draw_dealer_face_up_card()

    black_jack.draw_player_hand()
    choice = input("would you like to hit (y/n): ").lower()
    while choice == "y":
        black_jack.player_hit()
        black_jack.draw_player_hand()
        if sum(black_jack.total_value_player) > 21:
            break
        choice = input("would you like to hit (y/n): ").lower()
        if choice == "n":
            break
        else:
            continue
    
    black_jack.dealer_hit()
    black_jack.draw_dealer_hand()
    black_jack.check_if_winner()
    black_jack.draw_money()
    run_again = input("\nwould you like to bet again (y/n) ").lower()
    if run_again == "y":
        black_jack.bet = int(input("what would you like to bet (minimum bet of): "))
        while black_jack.bet < 20 or black_jack.bet > black_jack.current_money:
            black_jack.bet = int(input("what would you like to bet (minimum bet of): "))
        black_jack.dealer_card.clear()
        black_jack.player_card.clear()
        black_jack.total_value_dealer = []
        black_jack.total_value_player.clear()

    else:
        running = False
        break
    
    



    




