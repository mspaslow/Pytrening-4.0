movies = {
    2000: {
        "Gladiator": {
            'director': 'Ridley Scott',
            'oscar': True
        },
        "Chocolat": {
            'director': 'Lasse Hallström',
            'oscar': False
        },
        "Crouching Tiger, Hidden Dragon": {
            'director': 'Ang Lee',
            'oscar': False
        },
        "Erin Brockovich": {
            'director': 'Steven Soderbergh',
            'oscar': False
        },
        "Traffic": {
            'director': 'Steven Soderbergh',
            'oscar': False
        }
    },
    2001: {
        "A Beautiful Mind": {
            'director': 'Ron Howard',
            'oscar': True
        },
        "Gosford Park": {
            'director': 'Robert Altman',
            'oscar': False
        },
        "In the Bedroom": {
            'director': 'Todd Field',
            'oscar': False
        },
        "The Lord of the Rings: The Fellowship of the Ring": {
            'director': 'Peter Jackson',
            'oscar': False
        },
        "Moulin Rouge!": {
            'director': 'Baz Luhrmann',
            'oscar': False
        }
    },
    2002: {
        "Chicago": {
            'director': 'Rob Marshall',
            'oscar': True
        },
        "Gangs of New York": {
            'director': 'Martin Scorsese',
            'oscar': False
        },
        "The Lord of the Rings: The Two Towers": {
            'director': 'Peter Jackson',
            'oscar': False
        },
        "The Pianist": {
            'director': 'Roman Polański',
            'oscar': False
        }
    },
    2003: {
        "The Lord of the Rings: The Return of the King": {
            'director': 'Peter Jackson',
            'oscar': True
        },
        "Lost in Translation": {
            'director': 'Sofia Coppola',
            'oscar': False
        },
        "Master and Commander: The Far Side of the World": {
            'director': 'Peter Weir',
            'oscar': False
        },
        "Mystic River": {
            'director': 'Clint Eastwood',
            'oscar': False
        },
        "Seabiscuit": {
            'director': 'Gary Ross',
            'oscar': False
        }
    },
    2004: {
        "Million Dollar Baby": {
            'director': 'Clint Eastwood',
            'oscar': True
        },
        "The Aviator": {
            'director': 'Martin Scorsese',
            'oscar': False
        },
        "Finding Neverland": {
            'director': 'Marc Forster',
            'oscar': False
        },
        "Ray": {
            'director': 'Taylor Hackford',
            'oscar': False
        },
        "Sideways": {
            'director': 'Alexander Payne',
            'oscar': False
        }
    }
}

oscar_winners = []
for x in movies:
    filmy = movies[x]
    for y in filmy:
        if filmy[y]['oscar']:
            oscar_winners.append(y)

print(oscar_winners)

oscar_winners2 = []
for x in movies:
    for y in movies[x]:
        if movies[x][y]['oscar']:
            oscar_winners2.append(y)
print(oscar_winners2)