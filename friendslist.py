import os.path

friendsLogs = "C:\\Users\\jayde\\Desktop\\10pi Hackathon\\FriendsList.txt"

class friend:

    def __init__(self, name, points, friendsList):
        self.name = name
        self.points = int(points)
        self.friendsList = list(friendsList)

    def add_points(self, points):
        self.points += points

    def add_friends(self, friend):
        self.friendsList.append(friend)

    def remove_friends(self, friend):
        self.friendsList.remove(friend)

    def leaderboard(self):
        print("Leaderboard:")
        sorted = self.friendsList
        sorted.append(self)
        sorted = bubbleSort(sorted)
        for i in sorted:
            print(f"{i.name}: {i.points}")

usersList = []

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def add_user():
    name = input("What is your name? ")
    points = int(input("How many points do you have? "))
    global person
    person = friend(name, points, [])
    usersList.append(person)

def available_friends(user):
    print("Available Friends:")
    for i in usersList:
        if i not in user.friendsList and i != user:
            print(i.name)

    

    
Jayden = friend("Jayden", 10, [])
usersList.append(Jayden)
Ethan = friend("Ethan", 20, [])
usersList.append(Ethan)


for i in range(int(input("How many users would you like to add? "))):
    add_user()

Jayden.add_friends(Ethan)
Jayden.leaderboard()

# for i in usersList: print(i.name, i.points)
# available_friends(Jayden)