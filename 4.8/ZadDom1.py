movie_list = {
    'Shrek': {
        'kategoria': ['animacja', 'komedia'],
        'rok': 2001,
        'reżyser': ['Vicky Jenson', 'Andrew Adamson']
    },
    'Iron Man': {
        'kategoria': ['akcja', 'sci-fi'],
        'rok': 2008,
        'reżyser': 'Jon Favreau'
    },
    'Toy Story': {
        'kategoria': ['animacja', 'komedia'],
        'rok': 1995,
        'reżyser': 'John Lasseter'
    },
    'Avatar': {
        'kategoria': 'sci-fi',
        'rok': 2009,
        'reżyser': 'James Cameron'
    },
    'Król Lew': {
        'kategoria': 'animacja',
        'rok': 1994,
        'reżyser': ['Rob Minkoff', 'Roger Allers']
    },
    'Edward Nożycoręki': {
        'kategoria': ['fantasy', 'dramat'],
        'rok': 1990,
        'reżyser': 'Tim Burton'
    },
    'Maska': {
        'kategoria': ['fantasy', 'komedia'],
        'rok': 1994,
        'reżyser': 'Chuck Russell'
    }
}
archiwum = {
    'E.T.': {
        'kategoria': ['przygodowy', 'sci-fi'],
        'rok': 1982,
        'reżyser': 'Steven Spielberg'
    },
    'Ojciec Chrzestny': {
        'kategoria': ['dramat', 'gangsterski'],
        'rok': 1972,
        'reżyser': 'Francis Ford Coppola'
    },
    'Gladiator': {
        'kategoria': ['dramat', 'historyczny'],
        'rok': 2000,
        'reżyser': 'Ridley Scott'
    },
    'Czarnoksiężnik z OZ': {
        'kategoria': ['fantasy', 'musical', 'przygodowy'],
        'rok': 1939,
        'reżyser': ['King Vidor', 'Mervyn LeRoy']
    }
}

film = input("Podaj film: ")
if film in movie_list:
    print("Film jest już w bazie")
else:
    cat = input("Podaj kategorię filmu: ")
    year = input("Podaj rok produkcji: ")
    director = input("Podaj reżysera: ")
    movie_list[film] = {'kategoria': cat, 'rok': year, 'reżyser': director}

del movie_list['Iron Man']
archiwum['Iron Man'] = {
        'kategoria': ['akcja', 'sci-fi'],
        'rok': 2008,
        'reżyser': 'Jon Favreau'
    }

print(movie_list)
print(archiwum)

