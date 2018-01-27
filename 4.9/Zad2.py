countries = {
    "pl": "Witaj %s",
    "en": "Hello %s",
    "de": "Hallo %s",
    "it": "Ciao, %s",
    "fr": "Salut, %s"
}

def welcome():
    name = input("Jak masz na imie? ")
    country = input("Skąd pochodzisz? ")
    if country in countries:
        print(countries[country] %(name))
    else:
        print("Sorry, nie znam takiego kraju")
        print(countries['en'] %(name))

welcome()

def ask(question):
    answer = input(question)

def welcome2