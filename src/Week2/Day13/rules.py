import random


class Roll:
    rolls = {
        'paper': {'loose_to': 'scissors', 'win': 'rock'},
        'rock': {'loose_to': 'paper', 'win': 'scissors'},
        'scissors': {'loose_to': 'rock', 'win': 'paper'}
    }

    # def __init__(self, name, loose, win):
    #     self.__name = name
    #     self.__loose = loose
    #     self.__win = win
    #
    # def get_name(self):
    #     return self.__name.upper()

    # def __str__(self):
    #     return self.str_rep()

    # def str_rep(self):
    #     return f'Roll: {Roll.rolls}' #, Loose to: {self.__loose}, Win over: {self.__win}'


class Player:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

# class AI(Player):
#     pass
#     # def __init__(self, name):
#     #     self.name = name


class Game:
    def __init__(self):
        # self.rolls = {
        #     'paper': Roll(name='paper', loose='scissors', win='rock'),
        #     'rock': Roll(name='rock', loose='paper', win='scissors'),
        #     'scissors': Roll(name='scissors', loose='rock', win='paper')
        # }
        self.rolls = Roll.rolls

    def start_game(self):
        name = input("Player1, your name is: ")

        self.player1 = Player(name)
        self.player2 = Player('Computer')

        return '{}, {}'.format(self.player1, self.player2)

    def __get_roll(self, player):
        rps = self.rolls.keys()
        if player.get_name() != 'Computer':
            print()
            print(f'Choose rolls from:{list(rps)}')
            roll = input(f'{player.get_name()} your roll: ')
        else:
            roll = random.choice(list(rps))

        return roll

    def game_round(self):
        player1_roll = self.__get_roll(self.player1)
        print(f'{self.player1.get_name()} rolls {player1_roll}')
        player2_roll = self.__get_roll(self.player2)
        print(f'{self.player2.get_name()} rolls {player2_roll}')


game1 = Game()
game1.start_game()
game1.game_round()