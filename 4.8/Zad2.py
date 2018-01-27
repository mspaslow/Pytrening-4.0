week_days = ('poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela')
current_day = input("Jaki jest dzień tygodnia? ").lower()
"""
i = 7

while i > 0:
    i -= 1
    if week_days[i] == current_day:
        left = 4 - i
        if left <= 0:
            print("Yeah! dzis weekend")
        else:
            print("Do weekendu zostalo " + str(left) + " dni")
"""
i = 0
left = 4
while i < 7:
    if week_days[i] == current_day:
        if left <= 0:
            print("Yeah! dzis weekend")
        else:
            print("Do weekendu zostalo " + str(left) + " dni")
    i += 1
    left -= 1
