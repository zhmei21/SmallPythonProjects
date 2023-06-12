from xml.dom import minidom

# Parse the XML file
document = minidom.parse('exampleCars.xml')

# Prompt the user to specify the product type
userInput = input("Which product type should be displayed? ")

# Get a list of elements with the specified product type
productList = document.getElementsByTagName(userInput)

# Iterate over each product element
for product in productList:
    # Display the car label for each product
    print("Car:")
    
    # Iterate over the child nodes of the product element
    for value in product.childNodes:
        # Check if the node is an element node
        if value.nodeType == minidom.Node.ELEMENT_NODE:
            data = value.firstChild
            if data is not None:
                # Display the attribute name and value
                print("  " + value.tagName + ": " + data.nodeValue)
    
    # Add a newline to separate the displayed attributes of each car
    print("\n")

input("Exit")
