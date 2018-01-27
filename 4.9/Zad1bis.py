friends_home = {
    'Michal': 'Poznan',
    'Ola': 'Krakow',
    'Bartek': 'Berlin',
    'Tomek': 'Poznan'
}

while True:
    ask = input("Czy chcesz dodać kolejnego przyjaciela do listy? ")
    if ask == 'nie':
        break

    name = input("Jak ma na imię twój przyjaciel? ")
    city = input("Gdzie mieszka? ")

    if city in friends_home.values():
        print("nie potrzebuję więcej przyjaciół z", city)
    else:
        friends_home[name] = city
    print(friends_home)