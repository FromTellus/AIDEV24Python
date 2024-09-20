string = "Fornamn: Ulf Efternamn: Bjorkman"
ny_lista = string.split("Efternamn:")

nylista = ["hej", "jag", "heter", "ulf"]


versala_lista = []
for strang in ny_lista:
   versala_lista.append(strang.upper())
    
print(versala_lista)