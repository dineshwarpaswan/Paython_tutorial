print("del keyword:- Used to delet  object properties or object!")
# del s1.name <--object properties
# del s1 <--object 

class Student:
	def __init__(self,name, qulification,age):
		self.name = name
		self.qulification = qulification
		self.age = age

st = Student("Dineshwar","B.tech",35)

print(f"My name: [{st.name}] and Qulification: [{st.qulification}] and my age: [{st.age}]")
del st.age # object age properties will be delet
print(f"My name: [{st.name}] and Qulification: [{st.qulification}] and my age:[delet]")

print("Not show:",st.age)# <----name AttributeError:/properties has deleted, Result will be Erro Show

