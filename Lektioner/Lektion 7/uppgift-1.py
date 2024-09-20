import os  # Importera 'os'-modulen för att arbeta med operativsystemsfunktioner

# --- Introduktion ---
# Detta program utför följande:
# 1. Hämtar och visar den nuvarande arbetskatalogen.
# 2. Listar och visar alla filer och mappar i arbetskatalogen.
# 3. Skapar en mapp som heter 'backup' om den inte redan finns.

# --- Steg 1: Hämta den nuvarande arbetskatalogen ---
current_dir = os.getcwd()  # os.getcwd() returnerar sökvägen till den aktuella arbetskatalogen
print(f"Nuvarande arbetskatalog: {current_dir}")  # Skriver ut sökvägen

# --- Steg 2: Lista alla filer och mappar i arbetskatalogen ---
print("Innehåll i arbetskatalogen:")
files_and_dirs = os.listdir(current_dir)  # os.listdir() returnerar en lista över filer och mappar
for item in files_and_dirs:
    print(item)  # Skriver ut namnet på varje fil och mapp

# --- Steg 3: Skapa en ny mapp 'backup' om den inte redan finns ---
# Skapa sökvägen till 'backup'-mappen
backup_dir = os.path.join(current_dir, "backup")  # Kombinerar sökvägar på ett säkert sätt
print(f"Sökväg till 'backup'-mappen: {backup_dir}")  # Visar sökvägen

# Kontrollera om 'backup'-mappen redan finns
if not os.path.exists(backup_dir):  # os.path.exists() kontrollerar om en sökväg existerar
    os.mkdir(backup_dir)  # os.mkdir() skapar en ny mapp på den angivna sökvägen
    print("Mappen 'backup' har skapats.")  # Meddelande om att mappen skapades
else:
    print("Mappen 'backup' finns redan.")  # Meddelande om att mappen redan finns
