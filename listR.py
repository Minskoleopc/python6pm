# varaibles 
# arithmetic operator 
# comparison operator 
# logical operators 
# conditional statments 
# ternary operator 
# for loop
# while loop
# list


# list 
#         0      1       2        3       4
names = ["amol","raj","ramesh","satish","sam"]
print(names)
print(names[0])
names.append("sarika")
print(names)

#['amol', 'raj', 'ramesh', 'satish', 'sam', 'sarika']
names.pop()
print(names)
names.pop(2)
print(names)
# append() , pop() , pop(2)

# program 2
#          0         1       2       3
fruits = ["apple","mango","banana","orange"]
print(fruits)
e2 = fruits.index("mango")
print(e2)

fruits.remove("mango")
print(fruits)

# program 3
# append(), pop() , pop(2),index(),remove("mango") reverse() , sort()
marks = [11,22,33,44,55,11]
e2 = marks.count(11)
print(e2)

#              0       1         2           3
country = ["america","china","bangladesh","srilanka"]
print(country)
country.reverse()
print(country)

country.sort()
print(country)

# program 4
state = ["MH","UP","MP"]
state2 = ["KA","RJ"]

state.extend(state2)
print(state)

# state.clear()
# print(state)

print(state)
state.append("MZ")
state.insert(2,"JK")
print(state)


lst = [11,22,33]
# lstA = lst

# lst[1]= 44
# print(lst)
# print(lstA)

lstB = lst.copy()
lstB[1] = 222

print(lst)
print(lstB)

