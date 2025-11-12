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
    def __init__(self, name, __happiness, __energy, __hunger):
        self.name=name
        self.happiness=__happiness
        self.energy=__energy
        self.hunger=__hunger
       
    def play(self, act):
        self.act=act
        do=input(f"To play with {self.name}, type Play")
        while do.lower()=="play" or do.lower()=="continue":
            self.happiness+=10
            self.energy-=10
            self.hunger-=6
            print(f"{self.name} is now {self.act}")
            if self.energy<30:
                self.happiness-=20
            if self.energy<25:
                self.happiness-=30
            self.show_status()
            do=input(f"Continue, Eat, Sleep, or Stop")
        if do.lower()=="eat":
            self.food({"Dog Food"})
            do=input(f"Continue, Sleep, or Stop")
        elif do.lower()=="sleep":
            self.slep()
            do=input(f"Continue, Eat, or Stop")
        elif self.happiness==0 or self.happiness<0:
            self.dead() 
        elif self.energy==0 or self.energy<0:
            self.dead() 
        elif self.hunger==0 or self.hunger<0:
            self.dead() 


    def food(self, feed):
        self.feed=feed
        self.energy+=10
        self.hunger=100
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
        print(f"{self.name} is dead.")

Greg=pet("Greg", 50, 50, 50)
Greg.play({"Playing Fetch"})