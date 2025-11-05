""" #Lesson 1
class hero:
    def __init__(self, name, __money, inventory):
        self.name=name
        self.money=__money
        self.inventory=inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Ninja=hero("Ninja", 50, ["Ninja Stars"])
Ninja.buy({"title":"Sword", "atk":34, "value":25})
print(Ninja.__dict__)
 """

#Lesson 2
class pet:
    def __init__(self, name, happiness):
        self.name=name
        self.__happiness=happiness
        
    def play(self, act):
        action= [
            {
                "act": "fetch",
                "p":10
            },
            {
                "act": "bellyrubs",
                "p":15
            },
            {
                "act": "walking",
                "p": 5
            },
            {
                "act": "toys",
                "p":20
            }
        ]
        print(action)
        self.__happiness+=action
        print(f"{self.name} is playing {act}")

    def show_status(self):
        show=input("Want to know the pet's happiness. Yes or No")
        if show=="Yes":
            print(f"{self.name}'s happiness is now {self.__happiness}")

Greg=pet("Greg", 60)
do=input("To play with Greg, type Play, to find his happiness level, type Status, and to exit, type Close")
if do=="play".lower():
    


