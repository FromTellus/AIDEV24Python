import tkinter as tk

# Skapa fönstret
root = tk.Tk()

# Definiera funktionen som körs när knappen klickas
def on_click():
    print("Klickad!")

# Skapa en knapp och koppla den till funktionen
button = tk.Button(root, text="Klicka mig", command=on_click)
button.pack()

# Håll fönstret öppet
root.mainloop()
