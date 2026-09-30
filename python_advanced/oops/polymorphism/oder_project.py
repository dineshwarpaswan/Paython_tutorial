print("Letis Pratice : Create a class Order which store item & price. Use Dunder function __gt__() to convey that: order1 >order2 if price of order1>order2\n")


class Order:
	"""docstring for Order """
	def __init__(self, item, price):
		self.item = item
		self.price = price

	def storeItem(self):
		
		print(f"Item : {self.item} and Price: {self.price}")

	def __gt__(self, order2): # __gt__ is a Dunder function used (greter than)

		return self.price>order2.price

	def __lt__(self, order3): # __lt__ is a Dunder function used(les than)
		
		return self.price<order3.price


order1 = Order("Laptop",105000)
order2 = Order("Mobile",28000)
order3 = Order("Computer",15000)

order1.storeItem()
order2.storeItem()
order3.storeItem()

print(order1 > order2)
print(order1 < order2)
