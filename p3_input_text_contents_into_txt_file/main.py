class DiaryNgPanget:
	def __init__(self, file_name):
		self.file_name = file_name

	def write_diary(self):
		with open(self.file_name, "w") as diary_file:

			while True:
				line_entry = input ("Enter line: ")
				diary_file.write(line_entry + "\n")

				choose = input("Are there any additional lines? [Y/N]: ").upper()
				if choose == "N":
					break

		print("Saving diary entry...")
		print("Diary successfully saved in: " + self.file_name)

write_now = DiaryNgPanget("mylife.txt")
write_now.write_diary()
