from src.Week2.Day13.rules import Game


def print_header():
    print('------------------------')
    print('Rock Paper Scissors Game')
    print('------------------------')
    print()


def main():
    print_header()
    game1 = Game()
    game1.start_game()
    game1.game_round()


if __name__ == '__main__':
    main()
