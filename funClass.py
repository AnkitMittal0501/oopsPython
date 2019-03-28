class Car:
	"""
		blueprint for car
	"""

	def __init__(self, model, color, company, speed_limit):
		self.color = color
		self.company = company
		self.speed_limit = speed_limit
		self.model = model

	def start(self):
		print("started")

	def stop(self):
		print("stopped")
		print(self.color)
	def accelarate(self):
		print("accelarating...")
		"accelarator functionality here"
		
	def change_gear(self, gear_type):
		print("gear changed")
		" gear related functionality here"
maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
maruthi_suzuki.accelarate()
print(maruthi_suzuki.color)
maruthi_suzuki.stop()
audi = Car("A6", "red", "audi", 80)
