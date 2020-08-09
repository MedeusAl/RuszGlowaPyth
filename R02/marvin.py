paranoid_android = "Marvin"
letters = list(paranoid_android)
for char in letters:
    print('\t', char)

letters = "I'm C3PO. Robot protokolarny kawai!"
for char in letters [:6]:
    print('\t', char*2)
for char in letters [-7:]:
    print('\t'*2, char)
for char in letters [9:16]:
    print('\t'*3, char)