file = open("students1.txt", "w")
file.write("Paul\n")
file.write("Edouard\n")
file.write("Elodie\n")
file.close()

with open("students2.txt", "w") as file:
    file.write("Pauline\n")
    file.write("Gwendal\n")
    file.close()

with open("students2.txt", "a") as file:
    file.write("Edouard\n")
    file.write("Laurent\n")
    file.write("Maxime\n")
    file.close()

