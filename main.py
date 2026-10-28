class FamilyMember:
    def __init__ (self,eye_color,height):
        self.eye_color = eye_color
        self.height = height

    def Show_traits(self):
        print("Eye Color:",self.eye_color)
        print("Height is :",self.height)
    
class Kid(FamilyMember):
    def __init__(self,age,name,eye_color,height):
        self.age = age
        self.name = name
        super().__init__(eye_color,height)
    def Show_traits(self):
        print("Name:",self.name)
        print("Age :",self.age)
        super().Show_traits()


    def Favourite_Hobby(self,hobby):
        print(self.name,"Loves",hobby)


child = Kid("Maya",10,"Brown",140)

child.Show_traits()
child.Favourite_Hobby("Painting")

print("Is this kid a subclass :", issubclass(Kid,FamilyMember))





        