class HighestGWAFinder:
	def __init__(self, student_file, ranked_file):
		self.student_file = student_file
		self.ranked_file = ranked_file

	def rank_students(self):
		print(f"Initializing file reading process for {self.student_file}")

		with open(self.student_file, "r") as student_file:
			lines = student_file.readlines()

		student_data = lines[1:]

		print("Data loaded successfully!")
		print("Ranking students according to theit GWA...")

		for line in student_data:
			row = line.strip()
			if row != "":
				chopped_row = row.split(',')

			names = chopped_row[0]
			section = chopped_row[1]
			gwa = float(chopped_row[2])

			student_record = {
				"Name": names
				"Section": section
				"GWA": gwa
				}
			
