import requests

print("Welcome to your daily bite of wisdom!")

try:
    response = requests.get("https://zenquotes.io/api/random")
    response.raise_for_status()
    data = response.json()
    quote = data[0]['q']
    author = data[0]['a']
    print(f'"{quote}" - {author}')
except requests.exceptions.RequestException as e:
    print("Failed to retrieve quote. Please try again later.")