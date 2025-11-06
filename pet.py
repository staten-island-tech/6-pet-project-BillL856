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
why="true"
class pet:
    def __init__(self, name, happiness):
        self.name=name
        self.__happiness=happiness
    
        
    def play(self, act):
        self.act=act
        self.act= [
            {
                "act": "fetching",
                "p":10
            },
            {
                "act": "getting bellyrubs",
                "p":15
            },
            {
                "act": "going walking",
                "p": 5
            },
            {
                "act": "with toys",
                "p":20
            }
        ]
        
        print(self.act)
        do=input(f"To play with {self.name}, type Play, to find their happiness level, type Status, and to exit, type Close")
        while do.lower()=="play" or do.lower()=="continue":
            action=input(f"What do you want to do with {self.name}.")
            for e in self.act:
                if action.lower()==e["act"].lower():
                    self.__happiness+=e["p"]
                    print(f"{self.name} is {e}")
            do=input("Continue, or close, or show status")
        if do.lower()=="status":
            self.status=="Yes"
            do=input("Continue, or close")
        elif do.lower()=="close":
            why="false"


    def show_status(self, status):
        self.status=status
        if status=="Yes":
            print(f"{self.name}'s happiness is now {self.__happiness}")
Greg=pet("Greg", 60)

    

    

    


