vowels = set('aeoiyu')
insertWord = input("Podaj słowo, które chesz sprawdzić: ")
checkedWord = insertWord.lower()

samogloskiWSlowie = vowels.intersection(set(checkedWord))
print(samogloskiWSlowie)
