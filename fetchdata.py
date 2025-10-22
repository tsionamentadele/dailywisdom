import requests

print("Welcome to your daily bite of wisdom!")

response= requests.get("https://zenquotes.io/api/random")
if response.status_code == 200:
    data=response.json()
    quote=data[0]['q']
    author=data[0]['a']
    print(f'"{quote}" - {author}')
else:
    print("Failed to retrieve quote. Please try again later.")