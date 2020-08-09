# def search4vowels(word):
#     """funkcja sluzy do wyswietlania samoglosek w przekazanym przez uzytkownika slowie"""
#     vowels = set('aeuioiuy')
#     found = vowels.intersection(set(word))
#     for vowel in found:
#         print(vowel)

def search4vowels(phrase:str) -> set:
    """zwracanie samoglosek znalezionych w przekazanym łańcuchu znaków"""
    vowels = set('aeuioy')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str='aeyuio') -> set:
    """zwracanie podanych liter do znalezienia w przekazanym lancuchu znakow"""
    letters_to_be_checked = set(letters)
    return letters_to_be_checked.intersection(set(phrase))

print(search4vowels('mama'))

print(search4letters('konstantynoapolitankiewiczowna', 'xfg'))

print(search4letters('konstantynoapolitankiewiczowna'))

print(search4letters(letters='konstantynoapolitankiewiczowna', phrase='xfg'))