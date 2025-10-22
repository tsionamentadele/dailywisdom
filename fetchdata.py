import requests

print("Welcome to your daily bite of wisdom!")
while True: 
   
    try:
        response = requests.get("https://zenquotes.io/api/random")
        response.raise_for_status()
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        print(f'"{quote}" - {author}')
        want_to_save=input("Would you like to save this quote to a file? (yes/no): ").strip().lower()
        if want_to_save=="yes":
            with open("daily_quotes.txt","a") as file:
                file.write(f"Author: {author}\nQuote: {quote}\n\n")
                print("Quote saved successfully!")
        else:
            print("Quote not saved.")
        
        want_another=input("Would you like to receive a motivational quote? (yes/no): ").strip().lower()
        if want_another == "no":
            print("Thank you for using the quote generator. Have a great day!")
            break    
        
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve quote. Please try again later.")
