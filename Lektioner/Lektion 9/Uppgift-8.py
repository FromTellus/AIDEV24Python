def validera_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("Ogiltig e-postadress, den måste innehålla '@' och '.'")
    else:
        print("E-postadressen är giltig.")

try:
    email = input("Ange din e-postadress: ")
    validera_email(email)
except ValueError as e:
    print(e)
