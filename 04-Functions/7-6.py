def hide(card_number):
    card_number = str(card_number)
    lista = []
    for char in card_number:
            lista.append(char)
    for i in range(2, 12):
        lista[i] = "*"
    return ("".join(lista))    


print(hide(2039503496093423))