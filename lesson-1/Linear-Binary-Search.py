from jovian.pythondsa import evaluate_test_cases


def locate_card_BF (cards, query):
    
    for i in range(len(cards)): #percorrer toda a lista de maneira linear
        if cards[i] == query: #caso algum elemento da lista seja igual ao query
            return i # retornar a posição do elemento encontrado
    
    return -1


def locate_card_binary(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1  
        elif mid_number > query:
            lo = mid + 1
    
    return -1

    

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

evaluate_test_cases(locate_card_BF, tests)

evaluate_test_cases(locate_card_binary, tests)





