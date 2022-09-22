# ########## parameterised constructor ########

# class Employee:
#   def __init__(self,id,name,designation):
#     self.ID = id
#     self.Name = name
#     self.Designation = designation
#   def display(self):
#     print(self.ID,self.Name,self.Designation)

# E1=Employee(10,"John","HR")
# E1.display()

 
# ############## Without Parameters ###########
# class Employee:
#   def __init__(self):
#     pass
#   def display(self,ID,Name,Designation):
#     print(ID,Name,Designation)

# E1=Employee()
# E1.display(10,"John","HR")

########### task ##############
'''
class Company:
  def __init__(self):
    pass
  
  def display(self,ID,Name,totl_cust,tot_policy):
    print(ID,Name,totl_cust,tot_policy)

  def display(self,ID,Name,totl_policy,pan):
    print(ID,Name,totl_policy,pan)

  def display(self,ID,Name,salary,pan):
    print(ID,Name,salary,pan)

advisor = Company()
advisor.display(1041,"John",50,25)

customer = Company()
customer.display(1033,"Peter",55,"GPMJK654L")

employee = Company()
employee.display(1035,"Catherine",25000,"GHJKL9870L")

'''
################### Trainer ##################
'''
class User:
  def __init__(self):
    self.id = id
    self.name = nm
    self.totl_policy = tp
  
  def display(self,name,tp):
    return self.id,self.name,self.totl_policy

advisor = User(11001,"John",20)
advisor.total_cust=30
r1,r2,r3=advisor.display()
print(r1,r2,r3,advisor.total_cust)

customer = User(22001,"Peter",5)
customer.pan="LKJHN9807L"
r1,r2,r3=customer.display()
print(r1,r2,r3.customer.pan)

employee = User(33001,"Mark",50)
employee.pan="LUNHY9876O"
employee.salary=30000
employee.total_advisor= 10
r1,r2,r3 = advisor.display()
print(r1,r2,r3,employee.total_advisor,employee.salary, employee.pan)


'''

############################################### actual correct code
'''
class User:
  def __init__(self,id,nm,tp):
    self.id=id
    self.name=nm
    self.total_policy=tp

  def display(self):
    return self.id , self.name, self.total_policy
advisor=User(1011,'John',20)
advisor.total_cust=20
r1,r2,r3=advisor.display()
print(r1,r2,r3,advisor.total_cust)

customer=User(11,'Peter',5)
customer.pan='NJHK1452GHJ'
r1,r2,r3=customer.display()
print(r1,r2,r3,customer.pan)

employee=User(100,'Mark',50)
employee.total_advisor=10
employee.pan='LKJH1245UIO'
employee.sal=50000
r1,r2,r3=advisor.display()
print(r1,r2,r3,employee.total_advisor,employee.pan,employee.sal)

'''
######################################### adding multiple objects #############
# object_data=[]
# class User:
#   def __init__(self,id,nm,tp):
#     self.id=id
#     self.name=nm
#     self.total_policy=tp

#   def display(self):
#     return self.id , self.name, self.total_policy
  
#   def add(self,obj):
#     object_data.append(obj)

# id1=[]
# name=[]
# t_p=[]
# n=int(input("How many user's wants to add?"))
# for i in range(n):
#   id=input('enter id: ')
#   nm=input('enter name: ')
#   tp=input('enter total policy: ')
#   u1 = User(id,nm,tp)
#   u1.add(u1)
#   print("")
#   r1,r2,r3=u1.display()
#   id1.append(r1)
#   name.append(r2)
#   t_p.append(r3)
# print("")
# for i in range(len(id1)):
#   print(id1[i],name[i],t_p[i])


############public private protected ##########

'''
class Cup():
  def __init__(self):
    self._content_="Tea"
  def Fill(self):
    print(self._content_)

c=Cup()
c.Fill()

'''
##########################################
'''
from datetime import datetime
now=datetime.now()
print("repr representation of datetime: ",repr(now))
print("str representation of datetime: ",str(now))
'''
###########################################
'''
class Box():
        def __init__(self,x,y):
                self.x=x
                self.y=y
        def __str__(self):
                return "str value is'%s'"%self.x
        def __repr__(self):
                return "repr value is'%s'"%self.x
        def __del__(self):
                class_name = self.__class__.__name__
                print(class_name,"destroyed")
b1=Box(10,20)
print(str(b1)) # str representation
print(repr(b1)) # repr representation
b2=b1 # create 'b2' object
del b2 # delete 'b2' object
print(b1)
'''
########################################
'''
class Bird:
  color='brown'
  height='small'

class sparrow(Bird):
  look='tiny'

B1=Bird()
print(B1.color,B1.height)

s1=sparrow()
print(s1.color,s1.height,s1.look)
'''
####### multiple inheritance ########
'''
class BirdF:
  color='brown'
class BirdM:
  height='small'

class sparrow(BirdF,BirdM):
  look='tiny'

s1=sparrow()
print(s1.color,s1.height,s1.look)
'''

######################################

class Point:
  def __init__(self, x , y ):
    self.x = x
    self.y = y
  def __str__(self):
    return "Point(%d,%d)"%(self.x,self.y)
  def __add__(self,other):
    x = self.x + other.x
    y = self.y + other.y
    return Point(x,y)

p1=Point(2,3)
print('p1 data:',p1)
p2=Point(-1,2)
p3=p1+p2 # Call method by using operator
print(p3)
print(p1.__add__(p2)) # call method by name
print(Point.__add__(p1,p2)) # call method name with class



