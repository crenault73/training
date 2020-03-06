

# Utilisation de la boucle for :
for num_client in range(1,6):
    print("Vous etes le client numéro", num_client)

#Utilisation de la boucle for each

#Lister les emails :

#Blacklist :

blacklist=['tata1@gmail.com', 'tata2@gmail.com', 'tata3@gmail.com']

emails=['toto1@gmail.com', 'tata1@gmail.com', 'toto3@gmail.com']
for email in emails:
    if email in blacklist:
        print("Email {} interdit ".format(email))
        #continue
        break
    print("Email envoyé à ", email)

