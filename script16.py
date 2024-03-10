# int as parameter and int as return type
def addOne(x,y):
    return x + y
e = addOne(12,3)
print(e)

# float as parameter and float as return type 

def subTwo(x,y):
    return x - y
f = subTwo(12.3,12.1)
print(f)

# boolean as parameter and boolean as return type 
def canDrive(age,haveVehicle):
    if age > 18 and haveVehicle:
        return True
    else:
        return False
g = canDrive(19,True)
print(g)

# string as parameter and string as return type 
def greet(name):
    return ("welcome "+name)
j = greet("chinmay !")
print(j)

# list as parameter and list as return type 
names = ["chinmay","shirish","sameer","raj"]
def addName(lst):
    lst.append("vijeet")
    return lst
k = addName(names)
print(k)

# dictionary as parameter and dictionary as return type 
info = {
    "firstName":"chinmay",
    "lastName":"deshpande"
    #city:pune
}
def addCity(information):
    information['city'] = "pune"
    return information
l = addCity(info)
print(l)

# tuple as parameter and tuple as return type
numbers = (11,22,33)
def addValue(tupA):
    #(11,22,33)
    tupA = list(tupA)  # [11,22,33]
    tupA.append(44)  #[11,22,33,44]
    tupA = tuple(tupA) #(11,22,33,44)
    return tupA
l = addValue(numbers)
print(l)

# set as parameter and set as return type
setA = {11,22,33}
def addElement(seta):
    seta.add(44)
    return seta
z = addElement(setA)
print(z)

# function as parameter and function as return type
# teacher     --------> 30 k    ----------> living style 30k
# instagram   --------> 12 lpa  ----------> reels   







