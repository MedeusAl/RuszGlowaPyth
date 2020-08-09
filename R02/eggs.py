pharse = "podaj jajko!"
plist = list(pharse)
print(pharse)
print(plist)

# for letter in plist:
#     if letter == 'p':
#         plist.remove(letter)
#     elif letter == 'k':
#         plist.remove(letter)
for letter in range (len(plist),len(plist)-3,-1):
    plist.pop()
plist.remove('p')
plist.remove('a')
plist.remove('j')
new_pharse = ''.join(plist)
print(plist)
print(new_pharse)

print("====nowy przyklad====")

pharse = "podaj jajko!"
plist = list(pharse)
print(pharse)
print(plist)
firstStep = plist[1:7]
print(firstStep)
firstStep.insert(2, firstStep.pop())
firstStep.insert(2, firstStep.pop())
new_pharse = ''.join(firstStep)
print(new_pharse)
print(plist)