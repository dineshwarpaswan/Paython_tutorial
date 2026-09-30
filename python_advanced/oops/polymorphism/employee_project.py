class Employee:
    def __init__(self,role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
        
	
    def showDetails(self):
        print(f"My Role of :[{self.role}] and department [{self.dept}] amd my salary [Rs.{self.salary}]")

class Engineer(Employee):
    def __init__(self,name ,age):
    	self.name = name
    	self.age = age
    	super().__init__("Engineer","IT","85000")




emp = Engineer("DINESHWAR PASWAN",35)
emp.showDetails()


