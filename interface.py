 #Program interface should have all of these:
 #1. Tell the user what the program is and what it can do
 #2. Tell the user to make choices or select option
 #3. Let the user enter information, you should include a helpful message
 #4  Display the result or answer
 #5. Let the user close the program


teamlist = []
choice = ' '
while choice != 'X':
    print("TEAM MANAGER")
    print("=================")
    print("This program will help you manage your team")
    print("/n")
    print("A: Append a value")
    print("B: Print the teamlist")
    print("X: Exit program")
    choice = input("Enter your choice: ")
    if choice == 'A':
        name = input("Enter a name: ")
        teamlist.append(name)
print(teamlist)        


 