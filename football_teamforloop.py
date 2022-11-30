football_team = []

#append
for i in range(11):
    name = input("Add a player into the football team: ")
    football_team.append(i)
print(football_team)    

#edit and delete
repeat = 'Y'

while repeat == 'Y':

    edit = input('Which player do you want to change?: ')
    edit = int(edit)
    football_team[edit-1] = input('Enter a new player: ')
    print(football_team) 

    delete = int(input("Which player do you want to delete?: "))
    del football_team[delete-1]

    print(football_team) 
       
    

   


