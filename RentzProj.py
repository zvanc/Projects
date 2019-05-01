import random

class Card:

    def __init__(self, suit, value):
        self.suit   = suit
        self.value = value

    def afisaj(self):
        if self.value is 14:
            self.value = 'As'
        if self.value is 13:
            self.value = 'Rege'
        if self.value is 12:
            self.value = 'Dama'
        if self.value is 11:
            self.value = 'Valet'

        print('{} de {}'.format(self.value,self.suit))

class Deck(Card):

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for index_suit in ['Inima','Romb','Trefla','Pica']:
            for index_value in range(7,15): #As are cea mai mare valoare,14
                self.cards.append(Card(index_suit,index_value))

    def afisaj(self):
        for index in self.cards:
            index.afisaj()

    def shuffle(self):
        for index in range(len(self.cards)-1,0,-1):
            rand = random.randint(0,index)
            self.cards[index], self.cards[rand] = self.cards[rand], self.cards[index]

    def draw(self):
        return self.cards.pop()


class Player(Deck):

    num_players = 0

    def __init__(self,name):
        Player.num_players += 1
        self.name    = name
        self.hand    = []
        print('Jucator {}'.format(Player.num_players))

    def deal(self,deck):
         for i in range(8):
             self.hand.append(deck.draw())

    def afisaj_mana(self):
        for card in self.hand:
            card.afisaj()

    def discard(self):
        return self.hand.pop()

class Game(Player):

    def __init__(self):
        self.carti = []
        self.carti_value = []
        self.carti_suit  = []

    def carte_extrasa(self,carte):
        self.carti.append(carte)
        self.carti_value.append(carte.value)
        self.carti_suit.append(carte.suit)

    def afisaj_carti(self):
        for carte_index in self.carti:
            carte_index.afisaj()

    def choosed_game(self,game_choosed):
        if 'Rege rosu' == game_choosed:
            printf('---Rege rosu---')
            for card_index in range(Player.num_players):
                if self.carti_value[card_index] == 'Rege' and self.carti_suit[card_index] == 'Inima':
                    print('Jucatorul {} a pierdut'.format(card_index+1))
                    break

        if 'Zece de trefla' == game_choosed:
            pass

        if 'Dame' == game_choosed:
            print('---Dame---')
            for card_index in range(Player.num_players):
                if self.carti_value[card_index] == 'Dama':
                    print('Jucatorul {} a pierdut'.format(card_index+1))
                    break;

        if 'Carouri' == game_choosed:
            pass

        if 'Maini' == game_choosed:
            pass

        if 'Totale' == game_choosed:
            pass

        if 'Whist' == game_choosed:
            pass

        if 'Rentz' == game_choosed:
            pass



def main():

    deck = Deck()
    deck.shuffle()

    player1 = Player('Razvan')
    player1.deal(deck)
    player1.afisaj_mana()

    print('')
    print('')

    player2 = Player('Mike')
    player2.deal(deck)
    player2.afisaj_mana()

    print('')
    print('')

    player3 = Player('John')
    player3.deal(deck)
    player3.afisaj_mana()

    print('')
    print('')

    player4 = Player('Jim')
    player4.deal(deck)
    player4.afisaj_mana()

    print('')
    print('')


    joc = Game()
    joc.carte_extrasa(player1.discard())
    joc.carte_extrasa(player2.discard())
    joc.carte_extrasa(player3.discard())
    joc.carte_extrasa(player4.discard())
    joc.afisaj_carti()
    joc.choosed_game('Dame')

if __name__ == "__main__":
    main()