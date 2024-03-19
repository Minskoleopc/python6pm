
# program 1
lst = [1989,1990,1991,1992]
ages = []

for i in lst:
    x = 2024 - i
    ages.append(x)
print(ages)

a = list(map(lambda x:2024-x,lst))
print(a)
print([2024 - i for i in lst])

# program 2
f = lambda x : 2024 - x
f(lst[0])


# program3
names = ["chinmay","sarika","kajal","ninad"]
above5 = []
for x in names:
    if len(x) > 5:
        above5.append(x)
print(above5)

print([x for x in names if len(x) > 5])
e = list(filter(lambda x : len(x) > 5,names))
print(e)      
        

transactions = []
d = [2,3,4,-55,-66,77,44,555]
for x in d:
    if x < 0:
        #print("withdrawl")
        transactions.append("withdraw")
    else:
       transactions.append("deposit")
print(transactions)
print(["withdrawl" if x < 0 else "deposit" for x in d])
print(list(filter(lambda x : x > 0 , d)))
print(list(filter(lambda x : x < 0 , d)))

# decorator , recursive function , generators , modules


# collection --- 

# names = ["chinmay","sarika","poorva","mayuri"]
# info = {
#     "firstName":"chinmay",
#     "lastName":"deshpande"
# }
# tupleA = (22,33,44)
# set = {11,22,33,55,66,77}
# firstName = "chinmay"

# CRUD operation
# Methods
# Loop
# element present , duplicate







