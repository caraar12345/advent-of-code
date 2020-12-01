file=open("input.txt","r")
fileArray = file.readlines()
final = 0
results = []
while True:
    for x in fileArray:
        final += int(x.strip())
        if final not in results:
            results.append(final)
        else:
            print(final)
            exit()
        #print(results)
