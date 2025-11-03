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
        
            self.__happiness+=10

    def show_status(self):
        show=input("Want to know the pet's happiness. Yes or No")
        if show=="Yes":
            print(f"{self.name}'s happiness is now {self.__happiness}")
        