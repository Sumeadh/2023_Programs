'''
#Don't give inbuilt class names to define a classs
#giving arg as self is not mandatory
class Computer:
     def __init__(self,cpu,ram):
          print("init gets called automatically")
          self.o1=cpu #eventhough we passed cpu and ram in line 12, we never we never assigned them to our object called self
          self.o2=ram
          self.o3='personal computer'

     def config(self):
          self.o4='hi'
          print("Config is",self.o1, self.o2)          


com1 = Computer('i5', 16)  #  Computer('i5', 16)---> constructor
com2=Computer('Ryzen 3',8)
#com1 is an object of the class computer
print(type(com1))
a=5
print(a.bit_length())
# wheares a is an object of the class integer

Computer.config(com1) 
Computer.config(com2)

#another method to call the function
com1.config()
#Since we aldready mentioned the type of com1 the function config takes com1 as it's parameter
print(com1.o4)
'''
# variable type
'''

class Car:
    wheels= 4
    def __init__(self):
        self.mil=10
        self.com='BMW'

    @classmethod
    def change_wheels(cls):
          cls.wheels=8
          return cls.wheels
    
    @staticmethod
    def info():
        print('hi this is a static method')

c1=Car()
c2=Car()
# to change a instance variable, u can refer to the object varaible or the class name  
c1.mil=15
# To change a class variable only refer to the class name
Car.wheels=5
print(Car.change_wheels())
Car.info()

'''
# multiple class
'''

class A:
    def __init__(self):
        super().__init__()
        print('Yu reached A subclass')
class B:
     def __init__(self):
         print('Yu reached B subclass')
class C(A,B):
     def __init__(self):
         super().__init__()
        

         print('yu reached C mainclass')

a1=C()
'''
#operator over-riding
'''
class Student:
    def __init__(self,m1,m2) :
        self.o1=m1
        self.o2=m2
    
    def  __add__(self,other):
        c1=self.o1+other.o1
        c2= self.o2+other.o2
        s3=Student(c1,c2)
        return s3
    def __str__(self) -> str:
        return'{} {} '.format(self.o1,self.o2)
        #or just return self.m1,sellf. m2
s1=Student(20,60)
s2=Student(40,30)
s3=s1+s2 #Now s3 is also from  Student class
print(s3.o1)

print(s3)

'''
# Y use encapsulation

'''
class A:
    __tech1 = 'name'
    def __init__(self):
        print('Yu reached A subclass')
        self.__tech2='tech2 of A'

class B(A):
     def __init__(self):
         print('Yu reached B subclass')
o1=B()

print(o1._B__tech)
print(o1.tech2)

#setting nonpublic variable
o2=A()
o2._A__tech1='drake'
print(o2._A__tech1)
# an object of B can't access the tech variable of class A becz the class variable is encapsulated
'''

'''
class House:

	def __init__(self, price):
		self._price = price

	@property #getter method
	def price(self,key):
		return self._price,key

	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, int):
			self._price = new_price
		else:
			print("Please enter a valid price")

	@price.deleter
	def price(self):
		del self._price
		
ob=House(100)	
print(ob.price)

ob.price=50
print(ob.price)
'''
# https://realpython.com/python-getter-setter/  -----> REFER THIS ALSO
