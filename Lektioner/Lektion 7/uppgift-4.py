import datetime

# Hämta dagens datum och tid
current_date = datetime.datetime.now()
print(f"Dagens datum och tid: {current_date}")

# Skapa ett datumobjekt för julafton
christmas = datetime.datetime(current_date.year, 12, 24)

# Beräkna antalet dagar kvar till julafton
days_until_christmas = (christmas - current_date).days
print(f"Antal dagar kvar till julafton: {days_until_christmas}")
