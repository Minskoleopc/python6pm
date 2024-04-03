
# program 1

# compile time error

# def add():
# print(2+4)

# run time error 

# print("hello")
# e = int(input("please enter the numberA"))
# f = int(input("Enter the numberB"))
# print(e/f)
# print("bye")

# print("hello")
# numbers = [11,22,3,4,5,6]
# print(numbers[6])
# print("bye")

# logical error

# def calculateBonusSalary(amount):
#     return  amount * 0.10
# print(calculateBonusSalary(10000))

# program 2

# print("hello")
# try:
#     e = int(input("enter the number A"))
#     f = int(input("enter the number B"))
#     print(e/f)
# except Exception:
#     print("please enter correct input")
# print("bye")


# try  except  else  finally
# program 3
# print("hello")
# names = ["sarika","poorva","ninad","raj"]
# try:
#     e = int(input("enter the number A"))
#     f = int(input("enter the number B"))
#     print(e/f)
#     print(names[9])
# except ArithmeticError:
#     print("please enter correct input")
# except IndexError:
#     print("add more element to list")
# except Exception:
#     print("Please correct the values")
# print("bye")


# program 4

# print("hello")
# try:
#     e = int(input("enter the number A"))
#     f = int(input("enter the number B"))
#     print(e/f)
# except ArithmeticError:
#     print("please enter correct input")
# finally:
#     print("I will always execute")
# print("Bye")


# program 5
print("hello")
try:
    e = int(input("enter the number A"))
    f = int(input("enter the number B"))
    print(e/f)
except ArithmeticError:
    print("please enter correct input")
else:
    print("hello i will run")
finally:
    print("I will always execute")
print("Bye")

