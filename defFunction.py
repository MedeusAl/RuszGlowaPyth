def search4vowels(phrase:str) -> set:
    """zwracanie samoglosek znalezionych w przekazanym łańcuchu znaków"""
    vowels = set('aeuioy')
    return vowels.intersection(set(phrase))


def search4letters(phrase:str, letters:str='aeyuio') -> set:
    """zwracanie podanych liter do znalezienia w przekazanym lancuchu znakow"""
    letters_to_be_checked = set(letters)
    return letters_to_be_checked.intersection(set(phrase))
