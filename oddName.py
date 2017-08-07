""" David """


username = str(input("Enter username: "))
while username is "":
    print("No username entered.")
    username = str(input("Enter username: "))

for i in range(0,len(username),2):
    print(username[i], end= "")