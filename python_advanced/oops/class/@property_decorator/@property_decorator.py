print("Python Property:-We use @property on any method in the class to use the method as a property.\n")

class Subject:
	"""docstring for Subject"""
	def __init__(self, phy,che,math):
		
		self.phy = phy
		self.che = che
		self.math = math

		#self.Percentage = str((self.phy + self.che + self.math)/ 3)+"%"  # <-- type 1 ye fixde hai isme nahi udate hoga avgrage

	#def Show_Avarage(self):
	#	self.Percentage = str((self.phy + self.che + self.math)/ 3)+"%"    # < --- type 2 atomatic update ho jayega  avgrage

	#	return (f"Totale Avarage Marks in: {self.Percentage}")

	@property  		# <--decorater use
	def Show_Avarage(self):
		self.Percentage = str((self.phy + self.che + self.math)/ 3)+"%"  # <---type 3 atomatic update ho jayega avgrage
		return f"Total Avarage Marks in: {self.Percentage}"
	
		
sub = Subject(80,40,60)

#print("Totale :",sub.Percentage)
print(sub.Show_Avarage)  # fixed agrage :60

sub.phy = 200
print("Totale :",sub.Percentage) # nahi uppdate hoga : 60
print(sub.Show_Avarage) # new value ke sath update avrage :100
sub.math = 90
print(sub.Show_Avarage) # new value ke sath update avrage: 110

