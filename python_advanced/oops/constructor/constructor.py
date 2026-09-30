print("\n __init__ Function:- all class have called __init__(),which s always execute when the class is being initiated. The self parameter is a refference to the current instance of the class,and is used to access variables\n")

class Cars: # class name
	def __init__(): # defult constructor <lekin compalsery nahi hai, dono me se kewal ak hi pass hoga jis me parameterize hoga.
		pass
		
	def __init__(self, name, color):  #  parameterize constructor ya initilise 
		self.name = name  	
		self.color = color  
		#print("\nhello  my der freinds") # testing keliye use kiya gya tha ye bhi run ho jayega
	
Car = Cars("honda city","Red") # instantiating  class 
# access its propertis
print("THIS  is a : ",Car.name," CAR VERY SMART LOCK: ",Car.color,"COLOR")#<--instance(object) class  
print(Car.name)
print(Car.color)
print('')

# access its propertis
Car1 = Cars("Maruti Suzuki","Blue") # instantiating class 
print(Car1.name) 
print(Car1.color)
print([Car1.name, Car1.color]) #<--instance(object) class  
Car1.name = "Vegnur" # replace wille be
print("\nUpdate here in list:",[Car1.name, Car1.color]) # updat new instance(oject) clas attributes 
