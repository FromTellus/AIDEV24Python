# valuta_modul.py
def sek_till_usd(sek):
    växelkurs = 0.11  # 1 SEK = 0.11 USD<
    return sek * växelkurs

def sek_till_eur(sek):
    växelkurs = 0.095  # 1 SEK = 0.095 EUR
    return sek * växelkurs

def sek_till_gbp(sek):
    växelkurs = 0.085  # 1 SEK = 0.085 GBP
    return limit_decimal(sek * växelkurs)

def limit_decimal(input):
    return round(input, 2)  # Round to 2 decimal places