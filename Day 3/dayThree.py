
with open("./input.txt", "r") as File:
    lines = File.readlines()
    inp1 = [line.rstrip().lstrip() for line in lines]


def getScore(letter):
    ASCII = ord(letter)
    if ASCII >= 65 and ASCII < 97:
        return ASCII - 65 + 27
    return ASCII - 96


scores = []

for item in inp1:
    mid = len(item)//2
    halfOne = set(item[0:mid])
    halfTwo = set(item[mid:len(item)])
    common = halfOne.intersection(halfTwo).pop()
    scores.append(getScore(common))

print("Task 1")
print(sum(scores))

print("Task 2")

args = [iter(inp1)] * 3
groups = list(zip(*args))

newScores = []

for group in groups:
    backpack1 = set(list(group[0]))
    backpack2 = set(list(group[1]))
    backpack3 = set(list(group[2]))
    commonFirst = backpack1.intersection(backpack2)
    badge = backpack3.intersection(commonFirst)
    newScores.append(getScore(badge.pop()))

print(sum(newScores))
