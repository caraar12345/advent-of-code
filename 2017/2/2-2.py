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

def factors(x):
    factorList = []
    for i in range(1, x + 1):
        if x % i == 0:
            factorList.append(i)
    return factorList
inFile = fileReadIn('input.txt')
total = 0
sortedFile = []

for line in inFile:
    currentLine = []
    temp = []
    for item in line:
        temp.append(int(item))
    temp.sort(reverse=True)
    sortedFile.append(temp)

for line in sortedFile:
    for item in line:
        factorList = factors(item)
        #print(factorList)
        for num in factorList:
            if num in line:
                if num == item:
                    pass
                else:
                    #print(num,item,factorList)
                    total += item/num
                    break

print(total)

