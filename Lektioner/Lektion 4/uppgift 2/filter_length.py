# filter_length.py

def filter_length(lista, max_längd):
    ny_lista = []
    for sträng in lista:
        if len(sträng) <= max_längd:
            ny_lista.append(sträng)
    return ny_lista