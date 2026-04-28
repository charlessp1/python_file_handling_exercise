class HighestGWAFinder:
	def __init__(self, student_file, ranked_file):
		self.student_file = student_file
		self.ranked_file = ranked_file

	def rank_students(self):
		print(f"Initializing file reading process for {self.student_file}")

		with open(self.student_file, "r") as student_file:
			lines = student_file.readlines()

		header_row = lines[0]
		student_data = lines[1:]
		students = []

		print("Data loaded successfully!")
		print("Ranking students according to theit GWA...")

		for line in student_data:
			row = line.strip()
			if row != "":
				chopped_row = row.split(',')

			names = chopped_row[0]
			section = chopped_row[1]
			gwa = float(chopped_row[2])

			student = [gwa, names, section]
			students.append(student)

		print("Starting student ranking process...")

		students.sort()

		print("Ranking process complete. Saving data...")

		with open(self.ranked_file, "w") as ranked_file:
			ranked_file.write(header_row)

			for student in students:
				student_gwa = str(student[0])
				student_name = student[1]
				student_section = student[2]

				save_data = student_name + ',' + student_section + ',' + student_gwa + "\n"
				ranked_file.write(save_data)

		print("Saving complete! " + "File: " + self.ranked_file + " successfully generated.")

run_sorter = HighestGWAFinder("student_record.csv", "student_rankings.csv")
run_sorter.rank_students()
