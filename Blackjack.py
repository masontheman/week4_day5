import random 
class Cards:
    def __init__(self):
        self.check_set = set()
        pass
    def return_card(self):
        while True:
            generated_card = random.randint(1,53)
            if generated_card not in self.check_set:
                self.check_set.add(generated_card)
                if generated_card > 39:
                    return (generated_card-39)
                if generated_card > 26:
                    return (generated_card-26)
                if generated_card > 13:
                    return (generated_card-13)
                if generated_card:
                  return generated_card
            else:
                pass
class Hand:
    def __init__(self):
        self.hand = list()
        self.dealer_hand = list()
        self.add_card = Cards()
    def put_card_in_hand(self):
        self.hand.append(self.add_card.return_card())
        self.hand.append(self.add_card.return_card())
        #print(self.hand)
    def put_card_in_dealer_hand(self):
        self.dealer_hand.append(self.add_card.return_card())
        self.dealer_hand.append(self.add_card.return_card())
        print(self.dealer_hand[0])
    def put_another_card_in_hand(self):
        self.hand.append(self.add_card.return_card())
        print(self.hand)
    def put_another_card_in_dealer_hand(self):
        self.dealer_hand.append(self.add_card.return_card())
        print(self.dealer_hand)
    def count_player(self):
        x = 0
        print(self.hand)
        for xy in self.hand:
            x+=xy
        #print(f'player total {x}')
        return x
    def count_player2(self):
        x = 0
        #print(self.hand)
        for xy in self.hand:
            x+=xy
        #print(f'player total {x}')
        return x
    def count_dealer(self):
        y = 0
        for x in self.dealer_hand:
            y+=x
        #print(f'the dealers total {y}')
        return y
    def count_dealer2(self):
        y = 0
        for x in self.dealer_hand:
            y+=x
        #print(f'the dealers total {y}')
        return y
class Player(Hand):
    player_money = 1000
    def __init__(self):
        pass
    def hit_player(self):
        self.more_cards_question = input('Need another card? your life depends on it\n')
        while len(str(self.more_cards_question)) > 2:
            self.game1.put_another_card_in_hand()
            if self.game1.count_player() > 21:
                print('You blew your load pal time to die')
                self.player_money = 0
                return False
            self.more_cards_question = input('Dont be shy take another?\n')
        if  self.game1.count_player() > self.game1.count_dealer():
            print(f'the player wins, account doubled')
            self.player_money = self.player_money*2
            return True
        else: 
            print('click ... click ... pow')
            self.player_money = 0
            return False
class Dealer:
    def __init__():
        pass
class Rules:
    player_money = 1000
    def __init__(self):
        print('''Welcome ( . . )
         -----   
Beat the Casino to Live''')
        self.player_job = input('Choose a Job:\nAssasin, DrugLord, Hacker, Terrorist\n')
        player_input_to_end_game = 'yes'
        print(f'How much are you willing to throw down?\n{self.player_money} pesos in your account')
        while True:
            Player()
            self.game1 = Hand()
            self.game1.put_card_in_hand()
            self.game1.put_card_in_dealer_hand()
            self.game1.count_player()
            self.game1.count_dealer()
            if self.game1.count_player2() > 21:
                print('bust player')
                self.player_money = 0
            elif self.game1.count_dealer() > 21:
                print('bust dealer, account doubled')
                self.player_money = self.player_money*2
            elif self.game1.count_player2() == 21:
                print('Blackjack player')
                self.player_money = self.player_money*2
            elif self.game1.count_dealer() == 21:
                print('Blackjack dealer')
                self.player_money = 0
            else:
                Player.hit_player(self)
                player_input_to_end_game = input('continue?')
            if len(player_input_to_end_game)>2:
                continue
            else: break
        print(self.player_money)
game1 = Rules()