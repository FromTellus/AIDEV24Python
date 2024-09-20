# Importera Flask-klassen från flask-biblioteket
from flask import Flask  

# Skapa en instans av Flask-applikationen
# __name__ är ett speciellt variabelnamn i Python som representerar namnet på den nuvarande modulens namn
app = Flask(__name__)  

# Definiera en route för rot-URL ("/")
# När någon besöker rot-URL:en kommer funktionen hello() att anropas
@app.route("/")  
def hello():  
    # Returnera en enkel textsträng som svar
    return "Hello, World!"  

# Kontrollera om detta skript körs direkt (inte importeras som en modul)
if __name__ == "__main__":  
    # Starta Flask-applikationen
    # app.run() startar en inbyggd utvecklingsserver som lyssnar på port 5000 som standard
    app.run()