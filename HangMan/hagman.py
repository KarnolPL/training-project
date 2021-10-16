import sys
from words import rand_word

word = rand_word
used_letters = []
user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print(f"Pozostało prób: {num_of_tries}")
    print(f'Uzyte litery: {used_letters}')
    print()

for _ in word:
    user_word.append("_")

print('*'*30)
print('Poziomy trudnosci gry:\n'
    'Łatwy -> 9 prób\n'
    'Średni -> 6 prób\n'
    'Trudny -> 3 prób')
print('*'*30)

x = input('Wybierz 1 dla Łatwy, 2 dla Średni, 3 dla Trudny:')
if x == '1':
    number = 9
elif x == '2':
    number = 6
elif x == '3':
    number = 3


while True:
    num_of_tries = number
    letter = input('Podaj literę: ').lower()
    if not letter.isalpha():
        print('Podaj litere nie cyfre')
    elif len(letter) != 1:
        print('Podaj jedną litere')
    elif letter in used_letters:
        print('Ta litera była juz podana')
    else:
        used_letters.append(letter)

        found_indexes = find_indexes(word, letter)

        if len(found_indexes) == 0:
            print("Nie ma takiej litery.")
            num_of_tries -= 1
            

            if num_of_tries == 0:
                print("Przegrales! Koniec gry.")
                sys.exit(0)
        else:
            for index in found_indexes:
                user_word[index] = letter
            

            if ("".join(user_word)) == word:
                print('Brawo odgadłes poszukiwane słowo')
                sys.exit(0)

        show_state_of_game()


