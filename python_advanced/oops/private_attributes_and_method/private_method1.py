class Account:
	__name = "Anonymous" # private

	def __holder(self):
		print("HELLO Accoun!")
	
	def reset_p(self):
		self.__holder()

acc = Account()

print(acc.reset_p())# accesseble
print("\nHELLO",acc.__holder()) # method not imposible access


