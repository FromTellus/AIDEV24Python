# filter_letter.py

def filter_letter(lista, bokstav):
    ny_lista = []
    for sträng in lista:
        if bokstav in sträng:
            ny_lista.append(sträng)
    return ny_lista

