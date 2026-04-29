class IntegersSquareCube:
	def __init__(self, source_file, double_file, triple_file):
		self.source_file = source_file
		self.double_file = double_file
		self.triple_file = triple_file

	def square_of_integers(self):
		print(f"Calculating square of integers in file: {self.source_file}")

		with open(self.source_file, "r") as source_file:
			
