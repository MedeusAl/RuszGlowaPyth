

vowels = ['a','e','i','o','u','y']
insertWord = input("Podaj słowo, które chesz sprawdzić: ")
checkedWord = insertWord.lower()

found = {
    # 'a': 0,
    # 'e': 0,
    # 'i': 0,
    # 'o': 0,
    # 'u': 0,
    # 'y': 0
}

for letter in checkedWord:
    if letter in vowels:
        if letter not in found:
            found[letter] = 0
#dwu wierszowy IF mozna zamienić na found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'znaleziono', v, 'raz(y).')