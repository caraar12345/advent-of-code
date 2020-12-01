file=open("input.txt","r")
fileArray = file.readlines()
final = 0
for x in fileArray:
    final += int(x.strip())

print(final)
