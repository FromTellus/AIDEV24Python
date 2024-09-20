import logging

# Konfigurera grundläggande loggning för att logga till en fil
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='program.log',  # Filen där loggarna sparas
                    filemode='w')  # 'w' skriver över filen varje gång; använd 'a' för att lägga till

# Informationsmeddelande
logging.info("Programmet har startat.")

# Varningsmeddelande
x = 10
if x > 5:
    logging.warning("Värdet på x är större än förväntat!")

# Felmeddelande
try:
    result = 10 / 0
except ZeroDivisionError:
    logging.error("Ett fel inträffade: Division med noll.")

# Informationsmeddelande när programmet avslutas
logging.info("Programmet avslutades.")
