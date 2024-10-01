import logging

logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

try:
    tal = int(input("Ange ett tal: "))
    resultat = 100 / tal
except Exception as e:
    logging.error(f"Ett fel inträffade: {e}")
    print("Ett fel inträffade, kolla loggfilen för detaljer.")