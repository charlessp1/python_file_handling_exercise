# Creating function to read the file
class OddEvenDetector:
	def __init__(self, main_file, even_file, odd_file):

		self.main_file = main_file
		self.even_file = even_file
		self.odd_file = odd_file

	def read_file(self):
		print(f"Initializing file reading process for: {self.main_file}...")
		with open(self.main_file, "r") as main_file:
			read_contents = main_file.readlines()
		print("Data loaded successfully!")

		while True:
			choice = input("\nDo you want to play a game? Y/N: ").upper()
			if choice == "Y":
				print("Game starting...")
				self.odd_even_game(read_contents)
				break
			elif choice == "N":
				print("Game cancelled. Sorting numbers automatically...")
				self.sort_file(read_contents)
				break
			else:
				print("Invalid input. Please try again with [Y/N]").upper()

	def odd_even_game(self, read_content):
		even_nums = []
		odd_nums = []
		score = 0

		print("---Welcome to Odd Even Game!---")
		print('Instructions: type "E" if the number displayed is even, type "O" if it is odd.')

		for line in read_content:
			number = line.strip()
			if number != "":
				number = int(number)
				ans = input(f"Is {number} even or odd?[E/O]: ").upper()
				if ans == "E":
					if number % 2 == 0:
						score +=1
						even_nums.append(number)
						print("You are correct!")
					else:
						print("Engk! You are wrong")
				elif ans == "O":
					if number % 2 != 0:
						score += 1
						odd_nums.append(number)
						print("You are correct!")
					else:
						print("Engk! You are wrong.")
				else:
					print("Invalid input! You are automatically wrong, try again!")

		print(f"Game complete! Final score: {score}")
		print("Extracting numbers to even.txt and odd.txt")

		with open(self.even_file, "w") as even_file:
			for num in even_nums:
				even_file.write(str(num) + "\n")

		with open(self.odd_file, "w") as odd_file:
			for num in odd_nums:
				odd_file.write(str(num) + "\n")

		print("Extraction complete!")

files = OddEvenDetector("numbers.txt", "even.txt", "odd.txt")
files.read_file()
