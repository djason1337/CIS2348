# Dominic Jason 2203959


def print_roster():
    print('\nROSTER')
    for key in sorted_keys:
        print(f'Jersey number: {key}, Rating: {players[key]}')


def print_roster_above(num):
    print(f'\nABOVE {num}')
    for key in sorted_keys:
        if int(players[key]) > int(num):
            if key in players:
                print(f'Jersey number: {key}, Rating: {players[key]}')


# Menu for making changes
def print_menu():
    print('\nMENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit\n')


if __name__ == "__main__":

    players = {}
    player1jersey = int(input('Enter player 1\'s jersey number:\n'))
    player1rating = int(input('Enter player 1\'s rating:\n'))
    players[player1jersey] = player1rating

    player2jersey = int(input('\nEnter player 2\'s jersey number:\n'))
    player2rating = int(input('Enter player 2\'s rating:\n'))
    players[player2jersey] = player2rating

    player3jersey = int(input('\nEnter player 3\'s jersey number:\n'))
    player3rating = int(input('Enter player 3\'s rating:\n'))
    players[player3jersey] = player3rating

    player4jersey = int(input('\nEnter player 4\'s jersey number:\n'))
    player4rating = int(input('Enter player 4\'s rating:\n'))
    players[player4jersey] = player4rating

    player5jersey = int(input('\nEnter player 5\'s jersey number:\n'))
    player5rating = int(input('Enter player 5\'s rating:\n'))
    players[player5jersey] = player5rating
    # Sort keys from lowest to highest
    sorted_keys = sorted(players)
    # Print roster function

    print_roster()

    while True:
        print_menu()
        option = input('Choose an option:\n')
        sorted_keys = sorted(players)
        if option == 'o':

            print_roster()
        elif option == 'a':
            player6jersey = int(input('Enter a new player\'s jersey number:\n'))
            player6rating = int(input('Enter the player\'s rating:\n'))
            players[int(player6jersey)] = int(player6rating)
            sorted_keys = sorted(players)
        elif option == 'd':
            delete_player = int(input('Enter a jersey number:'))
            del players[delete_player]
        elif option == 'u':
            updated_player = int(input('Enter a jersey number:'))
            updated_rating = int(input('Enter a new rating for player:'))
            players[updated_player] = updated_rating
        elif option == 'r':
            num = int(input('Enter a rating:'))
            print_roster_above(num)
        elif option == 'q':
            break
