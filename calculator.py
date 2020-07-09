import definitions
# The line above will let you separate your concerns by defining functions your calculator might use in a separate file.

print("Welcome to the Python Calculator\n\nWhat would you like to do?")
choice = input()

if choice == "add":
    print(definitions.add())
elif choice == 'subtract':
    print(definitions.subtract())
elif choice == 'multiply':
    print(definitions.multiply())
elif choice == 'divide':
    print(definitions.divide())
elif choice == 'simple':
    print(definitions.simple())



