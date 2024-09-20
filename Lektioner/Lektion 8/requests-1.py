import requests

response = requests.get("https://randomuser.me/api/")
print(response.status_code)  # Kontrollera om förfrågan lyckades
print(response.text)  # Visa svaret från API:t
