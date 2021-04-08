class Animal:
    animal_name=''
    can_fly=False
    lay_egg=False
    can_swim=False
    on_land=False

    def __init__(self,name,fly,egg,swim,land):
        self.animal_name=name
        self.can_fly=fly
        self.lay_egg=egg
        self.can_swim=swim
        self.on_land=land

    def Animal_Class(self):
        if self.lay_egg==False:
            return "MAMAl"
        elif self.can_fly == True:
            return "Bird"
        elif self.lay_egg==True and self.can_swim==True and self.on_land == False:
            return "Fish"
        elif self.lay_egg == True and self.can_swim==True and self.on_land==True:
            return "Amphibian"
        elif self.lay_egg==True and self.on_land==True and self.can_fly == False:
            return "Reptile"

    def __str__(self):
        print(self.animal_name," is a ",self.Animal_Class())


def main():
    animal_list = [Animal('Elephant',False,False,False,True),Animal('Frog',False,True,True,True),Animal('Falcon',True,True,False,False)]
    print("The animals enterd are: ")
    for animal in animal_list:
        animal.__str__()


main()

# Sample OutPut
# The animals enterd are:
# Elephant  is a  MAMAl
# Frog  is a  Amphibian
# Falcon  is a  Bird