with open("./input.txt", "r") as File:
    lines = File.readlines()
    inp1 = [line.rstrip().lstrip() for line in lines]

translation = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}

symbols = {
    'Rock': ['A', 'X'],
    'Paper': ['B', 'Y'],
    'Scissors': ['C', 'Z']
}

scores = {
    symbols['Rock'][1]: 1,
    symbols['Paper'][1]: 2,
    symbols['Scissors'][1]: 3,
    'Lost': 0,
    'Draw': 3,
    'Win': 6,
}


winConditions = [("A", "Y"), ("C", "X"), ("B", "Z")]

gameScores = []

for game in inp1:
    gameCondition = tuple(game.split(" "))
    if gameCondition in winConditions:
        score = scores[gameCondition[1]] + scores['Win']
    elif all(symbol in symbols[translation[gameCondition[1]]] for symbol in gameCondition):
        score = scores[gameCondition[1]] + scores['Draw']
    else:
        score = scores[gameCondition[1]] + scores['Lost']
    gameScores.append(score)

print("Part 1")

print(sum(gameScores))


scores = {
    symbols['Rock'][0]: 1,
    symbols['Paper'][0]: 2,
    symbols['Scissors'][0]: 3,
    'Lost': 0,
    'Draw': 3,
    'Win': 6,
}


winConditions = [('A', 'B'), ('B', 'C'), ('C', 'A')]

print("Part 2")

partTwoScores = []

for game in inp1:
    gameCondition = tuple(game.split(" "))
    if gameCondition[1] == "Y":
        score = scores['Draw'] + scores[gameCondition[0]]
        partTwoScores.append(score)

    elif gameCondition[1] == "X":
        # loose
        current = list(
            filter(lambda cond: cond[0] == gameCondition[0], winConditions))
        currentMove = current.pop()[1]
        nextMove = list(filter(
            lambda cond: cond != currentMove and cond != gameCondition[0], ['A', 'B', 'C']))
        nextMovePlayed = nextMove.pop()
        score = scores['Lost'] + scores[nextMovePlayed]
        partTwoScores.append(score)

    elif gameCondition[1] == "Z":
        current = list(
            filter(lambda cond: cond[0] == gameCondition[0], winConditions))
        currentMove = current.pop()
        score = scores['Win'] + scores[currentMove[1]]
        partTwoScores.append(score)

print(sum(partTwoScores))
