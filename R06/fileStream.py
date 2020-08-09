# todos = open('todos.txt', 'a')
# print('wykonaj czynnosc nr 1', file=todos)
# print('wykonaj zadanie nr 1', file=todos)
# print('sprawdz czy wykonales czynnosci i zadania', file=todos)
# todos.close()

print('------------------')

tasks = open('todos.txt')
for chore in tasks:
    print(chore, end='')
tasks.close()

print('------------------')

with open('todos.txt') as zadania:
    for chore in zadania:
        print(chore, end='')

