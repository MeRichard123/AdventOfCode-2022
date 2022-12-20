with open("./input.txt", "r") as File:
    lines = File.readlines()
    inp1 = [line.rstrip().lstrip() for line in lines][0]

maxLength = len(inp1)
window = 4


for i in range(maxLength - window):
    currentWindow = inp1[i-1:i+window-1]
    if len(set(currentWindow)) == 4:
        print(currentWindow)
        marker = i + 3 
        print(marker)
        break

window = 14

for i in range(maxLength - 14):
    currentWindow = inp1[i-1:i+window-1]
    if len(set(currentWindow)) == 14:
        marker = i + window - 1
        print(currentWindow)
        print(marker)
        break
    
