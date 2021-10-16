#Prosty program do wykonywania zsumowania liczb podanych przez użytkownika

t = input('Podaj ilość testów: ')
t = int(t)

if t > 0 and t <= 100:
    for k in range(1, (t + 1)):
        ilosc_liczb = input('Podaj ilosc liczb do zsumowania: ')
        liczby = input(f'Podaj {ilosc_liczb} liczby ')
        lista_liczb = liczby.split(' ')
        result = 0
        for liczba in lista_liczb:
            result += int(liczba)
        print(result)

        


