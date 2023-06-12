# Open the XML file in read mode
file = open('exampleCars.xml', 'r')

# Prompt the user to specify the tag to search for
userInput = input("Which tag do you want to search for? ")

# Construct the start and end tags based on user input
startTag = "<" + userInput + ">"
endTag = "</" + userInput + ">"

# Read the contents of the XML file
contents = file.read()

# Find the starting and ending positions of the specified tag
startIndex = contents.find(startTag) + len(startTag)
stopIndex = contents.find(endTag)

# Print the content between the start and end tags
print("Content of the Tag: \n" + contents[startIndex:stopIndex])

# Close the file
file.close()

input("Exit")
