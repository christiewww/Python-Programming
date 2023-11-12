#pizza madlibs

class pizza_input:
    person_adj = ""
    nationality = ""
    person_name = ""
    vegetable1 = ""
    vegetable2 = ""
    vegetable3 = ""
    meat1 = ""
    meat2 = ""
    def pizza_des(self):
        pizza_des =("Pizza was invented by the %s %s chef named %s."
                    "\nThe pizza with 3 vegertables an 2 kinds of meat is the most popular."
                    "\nThis client chooses %s, %s, and %s for the vegetables;"
                    "\nAlso, client chooses %s and %s for the meat."
                    "\nSuch an excellent choice!") % (self.person_adj, self.nationality, self.person_name, self.vegetable1, self.vegetable2, self.vegetable3, self.meat1, self.meat2)
        return pizza_des

pizza1 = pizza_input()
pizza1.person_adj = input("Please enter an adj for a person: ")
pizza1.nationality = input("Please enter a nationality: ")
pizza1.person_name = input("Please enter a person's name: ")
pizza1.vegetable1 = input("Please enter a kind of vegetable: ")
pizza1.vegetable2 = input("Please enter a second kind of vegetable: ")
pizza1.vegetable3 = input("Please enter a third kind of vegetable: ")
pizza1.meat1 = input("Please a kind of meat: ")
pizza1.meat2 = input("Please another kind of meat: ")

print(pizza1.pizza_des())