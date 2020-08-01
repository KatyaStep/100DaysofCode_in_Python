from src.Week2.Day13.rules import Player, AI, Roll
import random


def print_header():
    print('------------------------')
    print('Rock Paper Scissors Game')
    print('------------------------')
    print()


def get_rolls():

    rolls = [
        Roll(name='paper', loose='scissors', win='rock'),
        Roll(name='rock', loose='paper', win='scissors'),
        Roll(name='scissors', loose='rock', win='paper')
    ]

    return rolls


def get_player_name():
    # TODO: ask a player his/her name
    player = input("Player1, your name is: ")

    return player


def start_game(player1, player2, rolls):
    rps = []
    for roll in rolls:
        rps.append(roll.get_name())

    print()
    print(f'RPC Game between {player1.name} and {player2.name}')
    # print(f'Choose rolls from:{rps}')
    # print()

    player1_roll = input(f'{player1.name} your roll: ')
    player2_roll =

    print(player2_roll)
    #print(f'{player2.name} your roll: {player2_roll} ')


def define_winner(roll1, roll2, rolls):
    pass


def main():
    print_header()
    rolls = get_rolls()
    name = get_player_name()

    player1 = Player(name)
    player2 = AI('Computer')

    start_game(player1, player2, rolls)



if __name__ == '__main__':
    main()
