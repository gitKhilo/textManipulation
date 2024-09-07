with open('Story.txt', 'r') as file:
    lines = file.readlines()
    firstFour = lines[:4]
    
    for i in range(0, len(lines), 2):
        print(lines[i].strip())
    
    for i in range(1, len(lines), 2):
        print(lines[i].strip())

with open('Story.txt', 'w') as file:
    file.write("Once upon a time\n")
    file.write("\n")
    file.writelines(lines)

with open('First4.txt', 'w') as newFile:
    newFile.writelines(firstFour)

with open('Story.txt', 'a') as file:
    file.write("\n")
    file.write("\n")
    file.write("The End\n")
    
with open('First4.txt', 'r') as file:
    lines = file.readlines()

lines = lines[1:]

with open('First4.txt', 'w') as file:
    file.writelines(lines)
