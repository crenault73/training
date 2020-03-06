# for: Pour une valeur de départ(1), jusqu'à une valeur d'arrivée (5)
print("*************** Boucle for: ****************************")
for num_client in range(1, 6):
    print("Vous êtes les client N°{}".format(num_client))

# for each: Pour chaque valeur d'une liste donnée
emails = ["gravenilvec@gmail.com", "graven@gmail.com", "Gigi2K@gmail.com",
          "Gummer1er@gmail.com", "steelaxiss@graven.yt", "paul.personnic@gmail.com"]
blacklist = ["Gummer1er@gmail.com", "steelaxiss@graven.yt"]
print("*************** Boucle for each avec continue: *********")
for email in emails:
    if email in blacklist:
        print("e-mail {} interdit! Envoi impossible.".format(email))
        continue

    print("e-mail envoyé à: ", email)

print("*************** Boucle for each avec break: ************")
for email in emails:
    if email in blacklist:
        print("e-mail {} interdit! Envoi impossible.".format(email))
        break

    print("e-mail envoyé à: ", email)
