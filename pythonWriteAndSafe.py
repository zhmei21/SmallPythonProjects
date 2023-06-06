print("Writing and reading a file with the name: example.txt")
try:
    with open("example.txt", 'w') as file:
        userInput = input("Write something: ")
        file.write(userInput)
        file.write("\nEnd")

except Exception as e:
    print("An error has occured:", str(e))

try:
    with open("example.txt", 'r') as file:
        for line_num, content in enumerate(file, start=1):
            print("Line %d: %s" % (line_num, content))

except Exception as e:
    print("An error has occurred while reading the file:", str(e))

#f = open("example.txt", "r")
#lines = 1
#for content in f:
#    print("Line %d: %s"%(lines, content))
#    lines+= 1
#f.close()
