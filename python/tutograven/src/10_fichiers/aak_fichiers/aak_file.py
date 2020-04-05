
students_liste = ["Amira", "Sam", "Manel"]

with open("students.txt", "a+") as file:
    for student in students_liste:
        file.write(student + "\n")
    file.close()
