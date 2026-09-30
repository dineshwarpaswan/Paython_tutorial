print("\nThe try...except statement is used to handle exceptions(Errors). The try statement takes a block of codes to test for error. The except statement handel the exception(error).\n")

print("\ntry block: <--iske andar woh code likha jata hai jisme error aane ki change hota hai.")
print("\nexcept block: <--Agar try ke andar koi error aaye , toh code yahan jump kar jata aur crash hone ke bajaye aapka likha hua messege print kar deta hai.\n")

# <----Fortunately, errors can be handled in python
try:
	print(a)
except:
	print("\nAn error occurred.( Variable defined nahi hai.)") # error <-alert message keliye used kiya jata hai


tx = "\nHello computer world!" # code after the try...except will still be executed 
print(tx)# agar code try...except ke bad likhate ho to cod run kajayega lekin sahi hona chahiye.