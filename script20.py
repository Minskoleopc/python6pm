# class Person:

#     # fields or properties
#     first_name = "chinmay"
#     last_name = "deshpande"

#     # instance
#     def walk(self):
#         print("I am walking")

#     def talk(self):
#         print("I am talking")

# chinmay = Person()
# print(chinmay.first_name)
# print(chinmay.last_name)
# chinmay.walk()
# chinmay.talk()

# amol = Person()
# print(amol.first_name)
# print(amol.last_name)
# amol.walk()
# amol.talk()

# amol.first_name = "amol"
# amol.last_name = "rao"

# print(amol.first_name)
# print(amol.last_name)


# program 2
class PersonB:
    # constructor
    def __init__(self,fn,ln):
        self.first_name  = fn 
        self.last_name = ln 

    def talk(self):
        print("I am talking")
    
    def walk(self):
        print("I am walking")

amol = PersonB("amol","rao")
chinmay = PersonB("chinmay","deshpande")

print(amol.first_name)
print(amol.last_name)

print(chinmay.first_name)
print(chinmay.last_name)
chinmay.city = "pune"
print(chinmay.city)
#print(amol.city)


#Assignment
# Vehicle 
# type model
# start() , stop()







