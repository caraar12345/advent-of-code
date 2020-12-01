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

inFile = fileReadIn("input.txt")
sumList = []
comparison = None
for current in range(len(inFile[0][0])):
    if inFile[0][0][current] != comparison:
        #print(current)
        comparison = inFile[0][0][current]
    else:
        sumList.append(inFile[0][0][current])
        #print(sumList)
    try:
        ahh = inFile[0][0][current+1]
    except IndexError:
        if inFile[0][0][0] != comparison:
            #print(current)
            comparison = inFile[0][0][0]
        else:
            sumList.append(inFile[0][0][0])
            #print(sumList)

total = 0
for num in sumList:
    total += int(num)

print(total)
