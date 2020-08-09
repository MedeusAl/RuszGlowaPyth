samogloski = ['a','e','i','o','u']
slowo = input("Podaj slowo: ")
znalezione_samogloski = []
for letter in slowo:
    if letter in samogloski:
        if letter not in znalezione_samogloski:
            znalezione_samogloski.append(letter)
for samogloski in znalezione_samogloski:
    print(samogloski)
