# inheritance


# single inheritance

class Father:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)
    
class Son(Father):
    def  __init__(self, fn, ln,sn):
        super().__init__(fn, ln)
        self.sname = sn

    def displaySName(self):
        print(self.sname + self.lastName)
        
amol = Son("dilip","rao","amol")

print(amol.firstName)
print(amol.lastName)
amol.displayName()
amol.displaySName()


# multi-level  inheritance

class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayGname(self):
        print(self.firstName + self.lastName)
    
class Father(GrandFather):
    def  __init__(self, fn, ln,ffn):
        super().__init__(fn, ln)
        self.fname = ffn

    def displayFname(self):
        print(self.fname + self.lastName)

class Son(Father):
    def __init__(self, fn, ln, ffn,ssn):
        super().__init__(fn, ln, ffn)
        self.sname = ssn

    def displaySname(self):
        print(self.sname + self.lastName)

chinmayA = Son("manohar","deshpande","shirish","chinmay")

print(chinmayA.firstName)
print(chinmayA.lastName)
print(chinmayA.fname)
print(chinmayA.lastName)

chinmayA.displayFname()
chinmayA.displayGname()
chinmayA.displaySname()


# herarchical inheritance 

class Mother:

    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayMName(self):
        print(self.firstName + self.lastName)


class Son(Mother):
    def __init__(self, fn, ln ,ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def displaySName(self):
        print(self.sname + self.lastName)

class Daughter(Mother):
      def __init__(self, fn, ln ,ddn):
        super().__init__(fn, ln)
        self.dname = ddn

      def displayDName(self):
         print(self.dname + self.lastName)

chinmay = Son("kanchan","deshpande","chinmay")
sarika = Daughter("kanchan","deshpande","gauri")

print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.sname)
chinmay.displayMName()
chinmay.displaySName()

print(sarika.firstName)
print(sarika.lastName)
print(sarika.dname)
sarika.displayMName()
sarika.displayDName()

# multiple inheritance
class Mother:
    def __init__(self,fn,ln):
        print("mother constructor called")
        self.firstName = fn 
        self.lastName  = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Father:
    def __init__(self,fn,ln):
        print("father constructor called .....")
        self.firstName = fn 
        self.lastName  = ln

    def displayName(self):
        print(self.firstName + self.lastName)


class Son(Mother,Father):
    def __init__(self, fn, ln , ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def dislaySname(self):
        print(self.sname + self.lastName)


chinmay = Son("shirish","deshpande","chinmay")

        







