def gradingStudents(grades):
    newGrades = []
    for grade in grades:
        if (grade >= 38 and grade % 5 >= 3):
            newGrades.append(grade -grade % 5 + 5)
        else:
            newGrades.append(grade)
    return newGrades