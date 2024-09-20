import re

# Skapa en sträng med e-postadresser och annan text
text = "Kontakta oss på support@example.com eller sales@example.org."

# Definiera regex-mönstret för att hitta e-postadresser
# Förklaring av mönstret:
# \b: Markerar början på ett ordgräns (ser till att vi matchar e-postadresser som separata ord)
# [A-Za-z0-9._%+-]+: Matchar användarnamnet före @-tecknet. Tillåter bokstäver (A-Z, a-z), siffror (0-9), och vissa specialtecken (._%+-). "+" betyder att tecknen kan upprepas en eller flera gånger.
# @: Matchar exakt ett @-tecken (som skiljer användarnamnet från domänen).
# [A-Za-z0-9.-]+: Matchar domännamnet. Detta tillåter bokstäver, siffror, punkt (.) och bindestreck (-). "+" betyder att tecknen kan upprepas en eller flera gånger.
# \.: Matchar en punkt (.). Eftersom punkt är ett specialtecken i regex måste vi "escape" det med en backslash (\).
# [A-Z|a-z]{2,}: Matchar toppdomänen, som måste vara minst två tecken lång (t.ex. ".com" eller ".org"). Tillåter både stora och små bokstäver (A-Z, a-z).
# \b: Markerar slutet på ett ordgräns.
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Använd re.findall() för att hitta alla e-postadresser
emails = re.findall(pattern, text)

# Skriv ut alla hittade e-postadresser
print("Hittade e-postadresser:")
for email in emails:
    print(email)
