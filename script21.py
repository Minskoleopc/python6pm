

class Person:
    def __init__(self,fn,ln):
        self.firstName  = fn 
        self.lastName = ln

    def display_name(self):
        print(self.firstName + self.lastName)

amol = Person("amol","rao")
chinmay = Person("shirish","deshpande")   
print(amol.firstName)
print(chinmay.firstName)
print(chinmay.lastName)
print(amol.lastName)
chinmay.display_name()
amol.display_name()

# program 2

class Person2:
    country = "bharat"
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
    def displayName(self):
        print(self.firstName + self.lastName)

    @classmethod
    def changeCountry(cls,cnty):
        cls.country = cnty

amol = Person2("amol","rao")
chinmay = Person2("chinmay","deshpande")
ninad = Person2('ninad',"dani")

print(amol.firstName)
print(amol.lastName)
print(amol.country)
amol.country = "india"
print(amol.country)
print(chinmay.country)
print(ninad.country)
Person2.changeCountry("Hindustan")
print(amol.country)
print(chinmay.country)
print(ninad.country)












    