
def print_header():
    print('------------------------')
    print('Rock Paper Scissors Game')
    print('------------------------')
    print()

def main():
    print_header()
    rolls = get_rolls()
    name = get_players_name()

    player1 = Player(name)
    player2 = Player(name)
    game(player1, player2, roll)

if __name__ == '__main__':
    main()
