# class with static reference so that no need to use self keyword
class A:
    @staticmethod
    def display():
        print("I am in the class")


A.display()

# Class with no static method so that self keyword is req
class B:
    def display(self):
        print("same method name used")
    print("Can we create 2 classes in one module")

c=B()
c.display()

# usig object though python by default take object instance 
class C(object):
    def sub(self):
        print("this is class C with object used")
d=C()
d.sub()

# Using pass keyword when there is no body for class or method provided
class D():
    pass
x = D()
x.side = 14
print x.side

class clue(D):
    def display(self):
        print(x.side)

f=clue()
f.display()

# Class with function asking for parameter
class WithParam:
    def displayWithParam(self,a):
        print(a)
para=WithParam()
para.displayWithParam(5)

# class with only constructor
class WithConstruct():
    def __init__(self,name,age):
        self.name=name
        self.age=age
w=WithConstruct("ankit",30)
print(w.name)


# class with constructor and methods both
class WithMethodConstruct():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getname(self):
        print(self.name)
    def getage(self):
        print(self.age)

mc=WithMethodConstruct("ankit",30)
mc.getname()
mc.getage()

    
 
