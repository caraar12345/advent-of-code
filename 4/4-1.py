def fileReadIn(filename): #allows each files to be easily imported
    File = open(filename,"r")
    FileRead = File.readlines()
    File.close()
    Temp = []
    Final = []
    for x in FileRead: #formats list to be easily laid out with no \n etc
        Temp.append(x.strip())
    for y in range(len(Temp)): #separates space -separated values into individual items in lists
        Final.append(Temp[y].split(" "))
    return Final

inFile = fileReadIn('input.txt')
count = 0

for item in inFile:
    #print(item)
 #   temp = item.sort()
   # print(temp)
    invalid = False
    for x in range(len(item)):
        try:
            if sorted(item)[x] == sorted(item)[x+1]:
                invalid = True
            else:
                pass
        except IndexError:
            pass
    if invalid == False:
        #print("ahh")
        count += 1
