########## parameterised constructor ########

class Employee:
  def __init__(self,id,name,designation):
    self.ID = id
    self.Name = name
    self.Designation = designation
  def display(self):
    print(self.ID,self.Name,self.Designation)

E1=Employee(10,"John","HR")
E1.display()

 
############## Without Parameters ###########
class Employee:
  def __init__(self):
    pass
  def display(self,ID,Name,Designation):
    print(ID,Name,Designation)

E1=Employee()
E1.display(10,"John","HR")