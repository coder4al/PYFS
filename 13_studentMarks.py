# Getting students name
students = input("Enter the students names  :  ").split()
print("Students List : ", students)

# Getting 5 marks of each student from students
marks = []
for student in students:
    print("Enter the 5 marks of ", student, " : ", end="")
    marks.append([eval(m) for m in (input().split())])
print("Marks List : ", marks)

# Calculating total of 5 marks of each student
totals = []
for mark in marks:
    totals.append(sum(mark))
print("Total List : ", totals)

# Finding percentage for each total values
percents = []
for total in totals:
    percents.append(total/5)
print("Percentage List : ", percents)

# Printing each student record
index = 0
for student in students:
    print(student, "\t:\tTotal = ",totals[index], ",\tPercentage = ", percents[index])
    index += 1 
