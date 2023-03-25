with open("grades.txt", "r") as f1, open("passing_grades.txt", "w") as f2:
    grades = [int(line.strip()) for line in f1]
    passing_grades = [grade for grade in grades if grade >= 60]
    for grade in passing_grades:
        f2.write(str(grade) + "\n")
