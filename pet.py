#Lesson 1
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


#Lesson 2
class pet:
    def __init__(self, name, __happiness):
        self.name=name
        self.happiness=__happiness
        
    def play(self, act):
        act=["Pet", "Fetch", "Play with Toy"]
        EE=input("Play or No Play")

        