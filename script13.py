# program 1
# upper()
first_name = "chinmay"
print(len(first_name))
e = first_name.upper()
print(e)


# lower()
last_name = "Deshpande"
e2 = last_name.lower()
print(e2)


middle_name = "SHIRISH"
e3 = middle_name.isupper()
print(e3)

e4 = e2.islower()
print(e4)

# lower(), upper() , islower() ,isupper()
# program 2

city = "pune"
e5 = city.startswith("pu")
e6 = city.startswith("P")
print(e5)
print(e6)

e7 = city.endswith('e')
e8 = city.endswith('une')
print(e7)
print(e8)

city2 = "chandrapur"
e9 = city2.count('a')
print(e9)

# program 3

city3 = " wardha"
print(len(city3))
e10 = city3.lstrip()
print(e10)
print(len(e10))

city4 = " wardha "
print(len(city4))
e11 = city4.rstrip()
print(len(e11))

city5 = " wardha "
e12 = city5.strip()
print(len(e12))

# program 4
info = "I am learning javascript"
e13 = info.replace("javascript","python")
print(e13)
print(info)


# program 5
e14 = "123".isdigit() #  0 - 9
print(e14)

e15 = "1233#"
e16 = e15.isalpha()
print(e16)

e17 = e15.isalnum()
print(e17)


























