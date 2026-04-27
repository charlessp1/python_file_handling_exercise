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
			choice = input("/nDo you want to play a game? Y/N").upper()
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
		
