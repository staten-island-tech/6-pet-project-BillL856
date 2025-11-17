""" #Activity 1
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

#Activity 2
class pet:
    def __init__(self, name, __happiness, __energy, __hunger):
        self.name=name
        self.happiness=__happiness
        self.energy=__energy
        self.hunger=__hunger
       
    def play(self, act):
        self.act=act
        do=input(f"To play with {self.name}, type Play")
        while do.lower() or doing.lower() in ("play","continue"):
            self.happiness+=10
            self.energy-=6
            self.hunger-=3
            print(f"{self.name} is now {self.act}")
            if self.energy<30:
                self.happiness-=15
            elif self.hunger<20:
                self.happiness-=20
            self.show_status()
            self.dead()
            doing=input(f"Continue, Eat, or Sleep") 
            if doing.lower()=="eat":
                self.food({"Dog Food"})
                doing=input("Continue or Sleep")
            elif doing.lower()=="sleep":
                self.slep()
                doing=input("Continue or Eat")


    def food(self, feed):
        self.feed=feed
        self.hunger=100
        print(f"{self.name} is now eating {self.feed}")
        self.energy+=10
        self.happiness+=25
        self.show_status()

    def slep(self):
        self.energy=100
        self.hunger-=10
        self.happiness+=25
        self.show_status()

    def show_status(self):
        print(f"{self.name}'s happiness is now {self.happiness}")
        print(f"{self.name}'s energy is now {self.energy}")
        print(f"{self.name}'s hunger is now {self.hunger}")

    def dead(self):
        if self.hunger <= 0 or self.energy <= 0 or self.happiness <= 0:
            print(f"{self.name} is dead.")
            exit()

Greg=pet("Greg", 50, 50, 50)
Greg.play("Playing Fetch")