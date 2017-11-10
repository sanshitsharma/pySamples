#!/usr/bin/python

def passingMark(passMark, grades):
	gradeDict = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1}
	
	grades_incase = grades.upper()

	total_marks = 0.0
	num_grades = 0.0

	for char in grades_incase:
		try:
			total_marks += gradeDict[char]
		except:
			print "Invalid Grade"
			return False

		num_grades += 1

	print total_marks/num_grades
	if ( total_marks/num_grades >= passMark ):
		return True

	return False

def main():
	print passingMark( 2.5, "CD" )

if __name__ ==  "__main__":
	main()
