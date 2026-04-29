class IntegersSquareCube:
	def __init__(self, source_file, double_file, triple_file):
		self.source_file = source_file
		self.double_file = double_file
		self.triple_file = triple_file

	def square_of_integers(self):
		print(f"Initializing reading process for file: {self.source_file}")

		with open(self.source_file, "r") as source_file:
			source_content = source_file.readlines()

		print("Data loaded successfully! Calculating square of integers...")

		squared_numbers = []
		for line in source_content:
			clean_line = line.strip()
			if clean_line != "":
				num = int(clean_line)
				squared = num ** 2
				format = str(num) + " ** 2 = " + str(squared)
				squared_numbers.append(format)

		print("Calculation complete! Saving file...")

		with open(self.double_file, "w") as double_file:
			for answer in squared_numbers:
				double_file.write(answer + "\n")

		print(f"Saving complete! File name: {self.double_file}")
		choice = input("Initializing calculation of cubes: would you like to proceed? [Y/N]: ").upper()
		while True:
			if choice == "Y":
				self.cube_of_integers(source_content)
				break
			elif choice == "N":
				print("Exiting program...")
				break
			else:
				print("Invalid input, try again.")

	def cube_of_integers(self, source_content):
		print("Calculating cube of integers...")

		cubed_numbers = []
		for line in source_content:
			clean_line = line.strip()
			if clean_line != "":
				num = int(clean_line)
				cubed = num ** 3
				format = str(num) + " ** 2 = " + str(cubed)
				cubed_numbers.append(format)

		print("Calculation complete! Saving file...")

		with open(self.triple_file, "w") as triple_file:
			for answer in cubed_numbers:
				triple_file.write(answer + "\n")

		print(f"Saving complete! File name: {self.triple_file}")

calculate = IntegersSquareCube("integers.txt", "double.txt", "triple.txt")
calculate.square_of_integers()
