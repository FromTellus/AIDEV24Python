import krigare as krigare
import fiende as fiende
import vapen as vapen
import kamp as kamp

# Skapa en krigare och ett vapen
krigare = krigare.Krigare("Thor")
vapen1 = vapen.Vapen("Svärd", 20)

# Lägg till vapnet till krigaren
krigare.lägg_till_vapen(vapen1)

# Använd vapnet
krigare.använd_vapen()  # Output: Thor använder Svärd

# Skapa en fiende och ett annat vapen
fiende = fiende.Fiende("Jätte")
vapen2 = vapen.Vapen("Yxa", 20)

# Lägg till vapnet till fienden
fiende.lägg_till_vapen(vapen2)

# Använd vapnet
fiende.använd_vapen()  # Output: Jätte använder Yxa

# Skapa en kamp mellan krigaren och fienden
kamp = kamp.Kamp(krigare, fiende)

# Starta kampen
kamp.starta()

