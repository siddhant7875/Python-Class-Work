#wap to create dictionaries for below task and perform all the above operations on 
# each product in a supermarket is associated with its price.
#each student in a school is associated with their grade.
#each customes id in a company is associated with a customer name.

# Dictionary for each product in a supermarket associated with its price
products = {
    "Milk": 1.99,
    "Bread": 2.50,
    "Eggs": 3.20,
    "Butter": 2.75
}

# Dictionary for each student in a school associated with their grade
students = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "A",
    "Daisy": "C"
}

# Dictionary for each customer ID in a company associated with a customer name
customers = {
    101: "John Doe",
    102: "Jane Smith",
    103: "Emily Davis",
    104: "Michael Brown"
}

# Function to perform basic dictionary operations
def perform_operations(dictionary, name):
    print(f"Dictionary: {name}")
    print("Original:", dictionary)

    # Adding a new entry
    if name == "Products":
        dictionary["Cheese"] = 4.50
    elif name == "Students":
        dictionary["Eve"] = "B"
    elif name == "Customers":
        dictionary[105] = "Lily Johnson"
    
    print("After Adding:", dictionary)
    
    # Updating an existing entry
    if name == "Products":
        dictionary["Milk"] = 2.10
    elif name == "Students":
        dictionary["Alice"] = "A+"
    elif name == "Customers":
        dictionary[102] = "Jane Wilson"
    
    print("After Updating:", dictionary)
    
    # Retrieving an entry
    if name == "Products":
        print("Price of Bread:", dictionary.get("Bread"))
    elif name == "Students":
        print("Grade of Bob:", dictionary.get("Bob"))
    elif name == "Customers":
        print("Customer with ID 103:", dictionary.get(103))
    
    # Removing an entry
    if name == "Products":
        dictionary.pop("Eggs")
    elif name == "Students":
        dictionary.pop("Daisy")
    elif name == "Customers":
        dictionary.pop(104)
    
    print("After Removing:", dictionary)
    print("\n")

# Performing operations on each dictionary
perform_operations(products, "Products")
perform_operations(students, "Students")
perform_operations(customers, "Customers")
