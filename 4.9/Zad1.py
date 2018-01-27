friends_home = {
    'Michal': 'Poznan',
    'Ola': 'Krakow',
    'Bartek': 'Berlin',
    'Tomek': 'Poznan'
}
cities = []
for friend in friends_home:
    cities.append(friends_home[friend])

while True:
    ask = input("Czy chcesz dodać kolejnego przyjaciela do listy? ")
    if ask == 'nie':
        break

    name = input("Jak ma na imię twój przyjaciel? ")
    city = input("Gdzie mieszka? ")

    if city in cities:
        print("nie potrzebuję więcej przyjaciół z", city)
    else:
        friends_home[name] = city
    cities.append(city)

    print(friends_home)