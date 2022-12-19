with open("./input.txt", "r") as File:
    lines = File.readlines()
    inp1 = [line.rstrip().lstrip() for line in lines][0]

print(inp1)
