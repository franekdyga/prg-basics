def number_of_letters(text):
    lista_liter = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    lista_dwu = [['a', 0], ['b', 0], ['c', 0], ['d', 0], ['e', 0], ['f', 0],
         ['g', 0], ['h', 0], ['i', 0], ['j', 0], ['k', 0], ['l', 0],
         ['m', 0], ['n', 0], ['o', 0], ['p', 0], ['q', 0], ['r', 0],
         ['s', 0], ['t', 0], ['u', 0], ['v', 0], ['w', 0], ['x', 0],
         ['y', 0], ['z', 0]]

    text_no_spaces = text.replace(' ', '')

    print(text)
    for char in text_no_spaces: 
        t = char.lower()
        lista_index = lista_liter.index(t)
        lista_dwu[lista_index][1] += 1

    najwieksza_wartosc = 0
    najwieksza_litera = None

    for element in lista_dwu:
        litera = element[0]
        wartosc = element[1]

        if wartosc > najwieksza_wartosc:
            najwieksza_wartosc = wartosc
            najwieksza_litera = litera
            
    return (f'The number of letter {najwieksza_litera}: {najwieksza_wartosc}')


print(number_of_letters('You never get a second chance to make a first impression'))