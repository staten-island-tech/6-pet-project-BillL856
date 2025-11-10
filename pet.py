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
why=True
class pet:
    def __init__(self, name, __happiness):
        self.name=name
        self.happiness=__happiness
       
    def play(self):
        do=input(f"To play with {self.name}, type Play")
        while do.lower()=="play" or do.lower()=="continue":
            self.happiness+=10
            print(f"{self.name} is now playing fetch!")
            do=input(f"Continue or Stop")
            
    def show_status(self):
        print(f"{self.name}'s happiness is now {self.happiness}")
Greg=pet("Greg", 60)
Greg.play()
Greg.show_status