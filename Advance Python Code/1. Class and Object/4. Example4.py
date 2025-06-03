# Example 4
class Mobile:
	def __init__(self):
		print("I am from constructot")
		self.model = 'RealMe X'
		
	def show_model(self):
		price = 1000				# Local Varaible
		print("Model:", self.model, "and Price:", price)

realme = Mobile()

# Accessing Method from outside Class
realme.show_model()



