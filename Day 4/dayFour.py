with open("./input.txt", "r") as File:
    lines = File.readlines()
    inp1 = [line.rstrip().lstrip() for line in lines]


print("Part 1")

counter = 0
for pair in inp1:
    shifts = pair.split(",")
    shiftPairs = [tuple(map(int, shift.split("-"))) for shift in shifts]
    left, right = shiftPairs
    if right[0] >= left[0] and right[1] <= left[1] or left[0] >= right[0] and left[1] <= right[1]:
        counter += 1

print(counter)


print("Part 2")

inp2 = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".rstrip().lstrip().split("\n")

counter = 0

for pair in inp1:
    shifts = pair.split(",")
    shiftPairs = [tuple(map(int, shift.split("-"))) for shift in shifts]
    left, right = shiftPairs
    r = set(list(range(left[0], left[1]+1))
            ).intersection(set(list(range(right[0], right[1]+1))))
    if len(list(r)) >= 1:
        counter += 1

print(counter)
