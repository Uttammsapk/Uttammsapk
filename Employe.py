class Employee:
    raise_amount = 1.4
    def __init__(self,Fname,Lname,ID,level,salary):
        self.Fname = Fname 
        self.Lname = Lname 
        self.ID = ID
        self.level = level
        self.salary = salary
        self.email = Fname + "." + Lname + "@uttambasket.com"
    
    def fullname(self):
        return '{} {}'.format(self.Fname,self.Lname)
    
    def apply_raise(self):
        return (self.salary * self.raise_amount)



emp_1 = Employee("Himani","Pandey",123,"senior",30000)

emp_2 = Employee("Aashik","Sapkota",4314, "senior", 2000000)



print(emp_1.level)
print(emp_2.email)
print(emp_1.fullname())
emp_1.raise_amount = 3
print(emp_1.apply_raise())

print(emp_1.__dict__)

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_1.apply_raise())
