with open("./input.txt", "r") as File:
    lines = File.readlines()
    inp1 = [line.rstrip().lstrip() for line in lines]

fileTree = {}

testInput = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".rstrip().lstrip().split("\n")


currentDirectory = ""

for line in testInput:
    if not line.startswith("$"):
        fileTree[currentDirectory].append(line)

    command = line.split(" ")[1:]
    match command[0]:
        case "cd":
            argument = command[1]
            if argument == "..":
                continue
            
            currentDirectory = argument
            
            if not argument in fileTree.keys():
                fileTree[argument] = []
        case "ls":
            continue

for key in fileTree.keys():
    for line in fileTree[key]:
        if line.split(" ")[0] == "dir":
            fileTree[key][fileTree[key].index(line)] = {line.split(" ")[1]: fileTree[line.split(" ")[1]]}

filesOrganised = {'/': fileTree['/']}

sums = {}

def traverse(struct, key):
    if isinstance(struct, dict):
        for key, value in struct.items():
            traverse(value, key)
    if isinstance(struct, list):
        for item in struct:
            traverse(item, key)
    if isinstance(struct, str):
        if key in sums.keys():
            sums[key].append(int(struct.split(" ")[0]))
        else:
            sums[key] = [int(struct.split(" ")[0])]
        return

traverse(filesOrganised, "/")

print(filesOrganised)

for key,value in sums.items():
    sums[key] = sum(value)

#limits = list(filter(lambda s: sums[s] < 100000, sums.keys()))

for key,value in filesOrganised.items():
    if isinstance(value, dict):
        pass

''
output = 0
for item in limits:
    print(item)
    output += sums[item]

print(output)
'''

"""
ary = []

def traverseFileTree(array, dictionary):
    for key in array:
        dirTotal = 0
        if isinstance(dictionary[key], dict):
            traverseFileTree(key.keys(), key)
        elif isinstance(dictionary[key], list):
            for item in dictionary[key]:
                if isinstance(item, dict):
                    traverseFileTree(item.keys(), item)
                else:
                    dirTotal += item.split(" ")[0]
"""

def parse(d):
    for key, value in d:
        if isinstance(value, dict):
            parse(value.items())
        elif isinstance(value, list):
            for item in value:
                parse(item)
        else:
            return value.split(" ")[0]



