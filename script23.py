# program 1
# single inheritance 
# parent - constructor , child no constructor

# class Student:
#     def __init__(self,fn,ln,adharNo):
#         self.firstName = fn 
#         self.lastName = ln
#         self.adharNo= adharNo

#     def displayName(self):
#         print(self.firstName  + self.lastName)

# # amol = Student("amol","rao","123")
# # print(amol.firstName)
# # print(amol.lastName)
# # print(amol.adharNo)
# # amol.displayName()
        
# class Teacher(Student):
#     salary = 100000
#     def displaySalary(self):
#         print(self.salary)

# amolT = Teacher("amolT","raoT",123)
# print(amolT.firstName)
# print(amolT.lastName)
# print(amolT.adharNo)
# print(amolT.salary)

# amolT.displayName()
# amolT.displaySalary()

# program 2
# single inheritance
# class Student:

#     def __init__(self,fn,ln,adharNo):
#         self.firstName = fn 
#         self.lastName = ln 
#         self.adharNo = adharNo

#     def displayName(self):
#         print(self.firstName + self.lastName)

# class Teacher(Student):
#     def __init__(self, fn, ln, adharNo,salary):
#         super().__init__(fn, ln, adharNo)
#         self.salary = salary

#     def displaySalary(self):
#         print(self.salary)


# chinmayT = Teacher("chinmay","deshpande",123,343243243)
# print(chinmayT.firstName)
# print(chinmayT.lastName)
# print(chinmayT.adharNo)
# print(chinmayT.salary)

# chinmayT.displayName()
# chinmayT.displaySalary()
       
# program 3
# multi-level
class Student:
    def __init__(self,fn,ln,adharNo):
        self.firstName = fn 
        self.lastName = ln 
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self,fn,ln,adharNo,salary):
        super().__init__(fn,ln,adharNo)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

class Professor(Teacher):
    def __init__(self, fn, ln, adharNo, salary,spec):
        super().__init__(fn, ln, adharNo, salary)
        self.special = spec

    def displaySpecialization(self):
        print(self.special)

bharat = Professor("bharat","bhate",213,4543534,"hindi")
print(bharat.firstName)
print(bharat.lastName)
print(bharat.adharNo)
print(bharat.salary)
print(bharat.special)

bharat.displayName()
bharat.displaySalary()
bharat.displaySpecialization()



















