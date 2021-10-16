import sys
import random

wygrane = 0
remisy = 0
porazki = 0


print("Witamy w grze  PAPIER KAMIEŃ NOŻYCE")
print("Wybierz (k)amień, (p)apier, (n)ożyce lub (w)yjscie")
while True:
    print(f"Aktualny wynik wygrane: {wygrane}, remisy: {remisy}, porażki: {porazki}")
    while True:
        player_choice = input('')
        if player_choice == 'w':
            sys.exit
        elif player_choice == 'k' or player_choice == 'p' or player_choice == 'n':
            break
        else:
            print('Podaj litere k, p, n lub w')
    
    if player_choice == 'k':
        print('Kamień kontra...')
    elif player_choice == 'p':
        print('Papier kontra...')
    elif player_choice == 'n':
        print('Nożyczki kontra...')
    
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_pick = 'k'
        print('Kamień')
    elif random_number == 2:
        computer_pick = 'p'
        print('Papier')
    elif random_number == 3:
        computer_pick = 'n'
        print('Nożyczki')

    if computer_pick ==  player_choice:
        print('Mamy remis!!!')
        remisy += 1
    elif computer_pick == 'k' and player_choice == 'p':
        print('Wygrałes!!!')
        wygrane += 1
    elif computer_pick == 'p' and player_choice == 'n':
        print('Wygrałes!!!')
        wygrane += 1
    elif computer_pick == 'n' and player_choice == 'k':
        print('Wygrałes!!!')
        wygrane += 1
    elif computer_pick == 'k' and player_choice == 'n':
        print('Przgerałeś :(:(')
        porazki += 1
    elif computer_pick == 'n' and player_choice == 'p':
        print('Przgerałeś :(:(')
        porazki += 1
    elif computer_pick == 'p' and player_choice == 'k':
        print('Przgerałeś :(:(')
        porazki += 1



    
        
