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
    circleForwards = current + (len(inFile[0][0])//2)
##    if circleForwards > len(inFile[0][0]):
##        circleForwards -= len(inFile[0][0])
    try:
        go = circleForwards
        if inFile[0][0][circleForwards] != comparison:
            #print(current)
            comparison = inFile[0][0][circleForwards]
        else:
            sumList.append(inFile[0][0][circleForwards])
    except IndexError:
        go = inFile[0][0][circleForwards-len(inFile[0][0])] + " bad"
        if inFile[0][0][circleForwards-len(inFile[0][0])] != comparison:
            #print(current)
            comparison = inFile[0][0][circleForwards-len(inFile[0][0])]
        else:
            sumList.append(inFile[0][0][circleForwards-len(inFile[0][0])])
        #print(sumList)
        print(go)
##    try:
##        ahh = inFile[0][0][circleForwards]
##    except IndexError:
##        if inFile[0][0][circleForwards] != comparison:
##            #print(current)
##            comparison = inFile[0][0][0]
##        else:
##            sumList.append(inFile[0][0][0])
##            #print(sumList)

total = 0
for num in sumList:
    total += int(num)

print(total)
