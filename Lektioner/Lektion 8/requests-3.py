import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {'title': 'Test', 'meddelande': 'Hoppas det fungerar'}
response = requests.post(url, data=payload)

print(response.status_code)  # Kontrollera statuskoden för att se om POST-förfrågan lyckades
print(response.json())  # Visa svaret från API:t
