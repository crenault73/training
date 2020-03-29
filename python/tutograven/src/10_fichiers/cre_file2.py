students_list = ["Paul", "Edouard", "Elodie", "Pauline", "Gwendal", "Edouard", "Laurent", "Maxime"]

with open("students2.txt", "w") as file:
    for student in students_list:
        file.write(student + "\n")
    file.close()
