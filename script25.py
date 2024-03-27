#
# class Calculator:
#     # def addition(self,x,y):
#     #     print(x+y)

#     # def addition(self,x,y,z):
#     #     print(x+y+z)

#     # def addition(self,x,y,z,a):
#     #     print(x+y+z+a)

#     def addition(self , x = None , y = None , z = None , a = None):
#         if(x != None and y != None  and z != None  and a != None):
#             print(x+y+z+a)
#         elif(x != None and y != None and z != None):
#             print(x+y+z)
#         elif(x != None and y != None):
#             print(x+y)

# cal = Calculator()
# cal.addition(23,4)
# cal.addition(23,4,5)
# cal.addition(23,4,5,5)


# same class same method name , different signature

#class Addition:

    # def add(self,x,y):
    #     print(x+y)

    # def add(self,x,y,z):
    #     print(x+y+z)
    
    # def add(self,x,y,z,a):
    #     print(x+y+z+a)

#     def add(self,x = None , y  = None , z = None , a = None):
#             if  x != None and y != None and z != None and a != None :
#                   print(x+y+z+a)
#             elif x != None and y != None and z != None:
#                   print(x+y+z)
#             elif x != None and y != None:
#                   print(x+y)



# a = Addition()
# a.add(12,3)
# a.add(123,44,55)
# a.add(23,4,5,6)


# program 2

# class Dog:
#     def talk(self):
#         print("Bhow bhow")

# class Human:
#     def talk(self):
#         print("Hello hi")

# def call_talk(obj):
#     obj.talk()


# a = Human()
# b = Dog()

# call_talk(a)
# call_talk(b)


# program 3

class Dog:
    def talk(self):
        print("Bhow bhow")

class Human:
    def talk(self):
        print("Hello hi")

class Duck:
    def sound(self):
        print("quack quack")

def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.sound()

a = Human()
b = Dog()
c = Duck()

call_talk(a)
call_talk(b)
call_talk(c)











