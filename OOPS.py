'''class Person:
    def say_hello(self):
        print("HELLO")
from OOPS import Person
me=Person()
me.say_hello()

o/P:Hello
Hello'''
#--------------------
'''class Person:
    def greet(self,name='Person'):
        return "Hello {}".format(name)
from OOPS import Person
me=Person()
greeting=me.greet("Bhargvai Prathap")
print(greeting)
o/p:Hello Bhargavi prathap
*here self refers to object data of the person class.
'''
#----------------
'''class Person:
    def __init__(self,name):
        print("hhello00{}".format(name))
#from OOPS import Person
me=Person("Bhargvai")'''
#--------------
'''class Person:
    def __init__(self,fullname,place):
        self.name=fullname
        self.location=place
p=Person("Bhargavi","khammam")
print(p.name,p.location)
here self.name  means refering the data of class object'''
#-------------------
'''class Car:
    def __init__(self,color,acceleration):
        self.color=color
        self.acceleration=acceleration
        self.speed=0
    def accelerate(self):
        print("speeding up")
        self.speed+=self.acceleration
        
    def apply_breaks(self):
        print("slowing down")
        self.speed-=10

s=Car("black",60)
s.accelerate()
s.apply_breaks()
print(s.speed)
print(s.acceleration)
'''
#------------------------
class User:
    def __init__(self,name,mbl_no,address):
        self.name=name
        self.mbl_no=mbl_no
        self_address=address
        
        
        
class Bankaccount:
    def __init__(self,user_details):
        self.generate_account_no()
        self.balance=0
   
    def generate_account_no(self):
        import uuid
        self.account_no=str(uuid.uuid4())
    
    def deposit(self,amount):
        self.balance += amount
    
    def withdrawl(self,amount):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount
            
u = User("Teja",99999999,address="Khammam")
b=Bankaccount(u)
print(b.balance)

'''n=Bankaccount(u)
n.generate_account_no()
print(n.mbl_no,n.name,n.account_no,n.balance)'''
b.deposit(1000000)
b.withdrawl(50000000)
print(b.balance)
print(u.name)
        
