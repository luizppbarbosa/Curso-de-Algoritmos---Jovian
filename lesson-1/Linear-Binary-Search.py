def locate_card (cards, query):

    pass

tests = []

#querry não acontece nas extremidades da lista
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

#querry é o primeiro elemento
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

#querry é o último elemento
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# apenas uma carta
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

# lista de cartas não tem a carta desejada
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# lista de cartas está vazia
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# lista de cartas com valores repetidos
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# carta desejada está repedita na lista, achando a primeira ocorrência da carta desejada
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

print(tests)


"""if locate_card (**test['input']) == test['output']:
    print(True)
else: 
    print(False)"""


