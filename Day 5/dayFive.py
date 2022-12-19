from collections import deque as Queue

'''
[T] [V]                     [W]    
[V] [C] [P] [D]             [B]    
[J] [P] [R] [N] [B]         [Z]    
[W] [Q] [D] [M] [T]     [L] [T]    
[N] [J] [H] [B] [P] [T] [P] [L]    
[R] [D] [F] [P] [R] [P] [R] [S] [G]
[M] [W] [J] [R] [V] [B] [J] [C] [S]
[S] [B] [B] [F] [H] [C] [B] [N] [L]
 1   2   3   4   5   6   7   8   9 
'''

nine = Queue(['L', 'S', 'G'])
eight = Queue(['N', 'C', 'S', 'L', 'T', 'Z', 'B', 'W'])
seven = Queue(['B', 'J', 'R', 'P', 'L'])
six = Queue(['C', 'B', 'P', 'T'])
five = Queue(['H', 'V', 'R', 'P', 'T', 'B'])
four = Queue(['F', 'R', 'P', 'B', 'M', 'N', 'D'])
three = Queue(['B', 'J', 'F', 'H', 'D', 'R', 'P'])
two = Queue(['B', 'W', 'D', 'J', 'Q', 'P', 'C', 'V'])
one = Queue(['S', 'M', 'R', 'N', 'W', 'J', 'V', 'T'])

with open("./input.txt", "r") as File:
    lines = File.readlines()
    inp1 = [line.rstrip().lstrip() for line in lines]

stacks = {
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: nine
}

for instruction in inp1:
    _, moveAmount, _, moveFrom, _, moveTo = instruction.split(" ")
    for _ in range(int(moveAmount)):
        top = stacks[int(moveFrom)].pop()
        stacks[int(moveTo)].append(top)

output = ""
for stack in stacks.values():
    output += stack.pop()

print(output)

print("Part 2")

# reset stacks after popping for part 2
nine = Queue(['L', 'S', 'G'])
eight = Queue(['N', 'C', 'S', 'L', 'T', 'Z', 'B', 'W'])
seven = Queue(['B', 'J', 'R', 'P', 'L'])
six = Queue(['C', 'B', 'P', 'T'])
five = Queue(['H', 'V', 'R', 'P', 'T', 'B'])
four = Queue(['F', 'R', 'P', 'B', 'M', 'N', 'D'])
three = Queue(['B', 'J', 'F', 'H', 'D', 'R', 'P'])
two = Queue(['B', 'W', 'D', 'J', 'Q', 'P', 'C', 'V'])
one = Queue(['S', 'M', 'R', 'N', 'W', 'J', 'V', 'T'])

stacks = {
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: nine
}

for instruction in inp1:
    _, moveAmount, _, moveFrom, _, moveTo = instruction.split(" ")
    temp = Queue()
    for _ in range(int(moveAmount)):
        if len(stacks[int(moveFrom)]) > 0:
            top = stacks[int(moveFrom)].pop()
            temp.append(top)
    while len(temp) > 0:
        top = temp.pop()
        stacks[int(moveTo)].append(top)

output = ""
for stack in stacks.values():
    output += stack.pop()

print(output)
