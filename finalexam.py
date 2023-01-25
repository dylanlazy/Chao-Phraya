#Create a list of 5 cities
citylist = ['Bangkok', 'Paris', 'Berlin','New York', 'Moscow']

#Traverse the list
for i in range(len(citylist)):
    print(citylist[i])

#append a city to the list
new = input("Enter the name of a city: ")
citylist.append(new)
#delete a city from the list
delete = int(input("Which city do you want to delete from the list: "))
del citylist[delete]
#print all the cities
print(citylist)

  