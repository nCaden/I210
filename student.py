students = ["Alice", "Bob", "Charlie", "Daisy", "Ethan", "Fiona", "George", "Hannah", "Isaac", "Jasmine"]
file1 = open('students.txt', 'r')
lines = file1.readlines()
file1.close()
student_no = 0
for line in lines:
    student_no += 1
    print(student_no, line.strip())

file2 = open('sudent_names.txt', 'w')
for student in students:
    file2.write(str(student) + "\n")
file2.close()