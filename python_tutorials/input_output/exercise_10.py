import csv


def filter_passed_students(input_file, output_file):
    with open(input_file, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    passed_students = [row for row in rows if int(row[2]) >= 60]

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(passed_students)
