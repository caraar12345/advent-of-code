def fileReadIn(filename): #allows each files to be easily imported
    File = open(filename,"r")
    FileRead = File.readlines()
    File.close()
    Temp = []
    Final = []
    for x in FileRead: #formats list to be easily laid out with no \n etc
        Temp.append(x.strip())
    for y in range(len(Temp)): #separates comma-separated values into individual items in lists
        Final.append(Temp[y].split(","))
    return Final

inFile = fileReadIn('input.txt')
total = 0
for line in inFile:
    currentLine = []
    for item in line:
        currentLine.append(int(item))
    maxNum = max(currentLine)
    minNum = min(currentLine)
    current = maxNum - minNum
    total += current
print(total)

