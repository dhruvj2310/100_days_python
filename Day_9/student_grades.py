student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for i, (sdt, scr) in enumerate(student_scores.items()):
    if 91 <= scr <= 100:
        gr = "Outstanding"
    elif 81 <= scr <= 90:
        gr = "Exceeds Expectations"
    elif 71 <= scr <= 80:
        gr = "Acceptable"
    else:
        gr = "Fail"

    student_grades[sdt] = scr

print(student_grades)