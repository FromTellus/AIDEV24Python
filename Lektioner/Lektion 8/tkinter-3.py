import tkinter as tk

# Skapa fönstret
root = tk.Tk()

# Skapa ett textfält
entry = tk.Entry(root)
entry.pack()

# Definiera funktionen som körs när knappen klickas
def show_text():
    text = entry.get()
    print(text)

# Skapa en knapp och koppla den till funktionen
button = tk.Button(root, text="Visa text", command=show_text)
button.pack()

# Håll fönstret öppet
root.mainloop()
