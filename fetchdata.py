import requests
from colorama import Fore, Style

print("Welcome to your daily bite of wisdom!")
while True: 
   
    try:
        response = requests.get("https://zenquotes.io/api/random")
        response.raise_for_status()
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']

        color_code={
       "author": Fore.CYAN,
       "quote": Fore.YELLOW
   }
        print(f'{color_code["quote"]}"{quote}" - {color_code["author"]}{author}{Style.RESET_ALL}')
        want_to_save=input("Would you like to save this quote to a file? (yes/no): ").strip().lower()
        if want_to_save=="yes":
            with open("daily_quotes.txt","a") as file:
                file.write(f"Author: {author}\nQuote: {quote}\n\n")
                print("Quote saved successfully!")
        else:
            print("Quote not saved.")
        
        want_another=input("Would you like to receive a motivational quote? (yes/no): ").strip().lower()
        if want_another == "no":
            read_saved=input("want to read saved quotes? (yes/no): ")
            if read_saved=="yes":
                with open("daily_quotes.txt","r") as file:
                    saved_quotes=file.read()
                    for quote in saved_quotes.split("\n\n"):
                        print(quote)
                print("Thank you for using the quote generator. Have a great day!")
                break  
            else:
                print("Thank you for using the quote generator. Have a great day!")
                break  
        
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve quote. Please try again later.")
