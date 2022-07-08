import datetime
from colorama import Fore


def show_game_board():
    for i in range(3):
        for j in range(3):
            print(Fore.RED + game[i][j], end=' ')
        print()

def check():
    if game[0][0] == "X" and game[0][1] == "X" and game[0][2] == "X":
        print ('player 1 wins')
        exit()
    if game[0][0] == "O" and game[0][1] == "O" and game[0][2] == "O":
        print ('player 2 wins')
        exit()
    if game[1][0] == "X" and game[1][1] == "X" and game[1][2] == "X":
        print ('player 1 wins')
        exit()
    if game[1][0] == "O" and game[1][1] == "O" and game[1][2] == "O":
        print ('player 2 wins')
        exit()
    if game[2][0] == "X" and game[2][1] == "X" and game[2][2] == "X":
        print ('player 1 wins')
        exit()
    if game[2][0] == "O" and game[2][1] == "O" and game[2][2] == "O":
        print ('player 2 wins')
        exit()
    if game[0][0] == "X" and game[1][0] == "X" and game[2][0] == "X":
        print ('player 1 wins')
        exit()
    if game[0][0] == "O" and game[1][0] == "O" and game[2][0] == "O":
        print ('player 2 wins')
        exit()
    if game[0][1] == "X" and game[1][1] == "X" and game[2][1] == "X":
        print ('player 1 wins')
        exit()
    if game[0][1] == "O" and game[1][1] == "O" and game[2][1] == "O":
        print ('player 2 wins')
        exit()
    if game[0][2] == "X" and game[1][2] == "X" and game[2][2] == "X":
        print ('player 1 wins')
        exit()
    if game[0][2] == "O" and game[1][2] == "O" and game[2][2] == "O":
        print ('player 2 wins')
        exit()
    if game[0][0] == "X" and game[1][1] == "X" and game[2][2] == "X":
        print ('player 1 wins')
        exit()
    if game[0][0] == "O" and game[1][1] == "O" and game[2][2] == "O":
        print ('player 2 wins')
        exit()
    if game[2][0] == "X" and game[1][1] == "X" and game[0][2] == "X":
        print ('player 1 wins')
        exit()
    if game[2][0] == "O" and game[1][1] == "O" and game[0][2] == "O":
        print ('player 2 wins')
        exit()


game = [['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]
show_game_board()
d1= datetime.datetime.now()
while True:
    
    print(Fore.GREEN +'player 1')
    
    while True:
        row = int(input('satr ra vared kon: '))
        col = int(input('sotoon ra vared kon: '))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col]== '-':
                game[row][col] = Fore.GREEN + 'X'
                break
            else:
                print('cell is not empty!')
        else:
            print('index out of range, try again!')
    show_game_board()
    check()
    
    print(Fore.YELLOW +'player 2')

    while True:
        row = int(input('satr ra vared kon: '))
        col = int(input('sotoon ra vared kon: '))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col]== '-':
                game[row][col] = Fore.YELLOW + 'O'
                break
            else:
                print('cell is not empty!')
        else:
            print('index out of range, try again!')
    show_game_board()
    check()



d2= datetime.datetime.now()
d = d2-d1
print(d)

