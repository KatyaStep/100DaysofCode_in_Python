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
    def __init__(self, name, score):
        self.__name = name
        self.score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.score



class Game:
    def __init__(self):
        self.rolls = Roll.rolls
        self.player1 = None
        self.player2 = Player('Computer', 0)

    def start_game(self):
        name = input("Player1, your name is: ").capitalize()

        self.player1 = Player(name, 0)
        # self.player2 = Player('Computer')

        return '{}, {}'.format(self.player1, self.player2)

    def __get_roll(self, player):
        rps = self.rolls.keys()
        if player.get_name() != 'Computer':
            print()
            print(f'Choose rolls from:{list(rps)}')
            roll = input(f'{player.get_name()} your roll: ').lower()
        else:
            roll = random.choice(list(rps))

        return roll

    def game_round(self):
        round_number = 3
        count = 0

        while count != round_number:
            print()
            print(f"----------Round {count+1}----------")
            try:
                player1_roll = self.__get_roll(self.player1)
                print(f'{self.player1.get_name()} rolls {player1_roll}')
                player2_roll = self.__get_roll(self.player2)
                print(f'{self.player2.get_name()} rolls {player2_roll}')

                # Get a winner of the round
                self.define_round_winner(player1_roll, player2_roll, self.rolls)
                count += 1
            except KeyError:
                print('Sorry, you typed a wrong roll. Try it again.')
                continue

        # Get a result of the Game
        self.define_game_winner(self.player1.get_score(), self.player2.get_score())

    def define_round_winner(self, roll1, roll2, rolls):
        print()

        if roll2 == roll1:
            print("It's a tie")
            print(f'{self.player1.get_name()}: {self.player1.get_score()}; '
                  f'{self.player2.get_name()}: {self.player2.get_score()}')

            return False

        elif roll2 == rolls[roll1]['win']:
            self.player1.score += 1
            print(f'{self.player2.get_name()} lost to {self.player1.get_name()}')
            print(f'{self.player1.get_name()}: {self.player1.get_score()}, '
                  f'{self.player2.get_name()}: {self.player2.get_score()}')

            return True

        else:
            self.player2.score += 1
            print(f'{self.player1.get_name()} lost to {self.player2.get_name()}')
            print(f'{self.player1.get_name()}: {self.player1.get_score()}, '
                  f'{self.player2.get_name()}: {self.player2.get_score()}')

            return True

    def define_game_winner(self, pl1_score, pl2_score):
        print()
        print("-------------------------")

        if pl1_score == pl2_score:
            print("Congratulations. It's tie!")
            return True
        elif pl1_score > pl2_score:
            print(f"{self.player1.get_name()} won the game! ")
            return True
        else:
            print(f"{self.player2.get_name()} won the game! ")
            return True


# game1 = Game()
# game1.start_game()
# game1.game_round()
