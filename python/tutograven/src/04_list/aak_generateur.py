from random import shuffle

# <=>

chaine=input("Entrer une chaine de la forme mot1/mot2/mot3/.... : ").split("/")

print(chaine)

length=len(chaine)
#shuffle(chaine)
#1/2/3/4/5/6/7/8/9/10print(chaine)
print("la taille de votre chaine est de {} mots ".format(length))

if length < 10:

    print("Les deux premiers mots sont {}".format(chaine[0:2]))
else:
    print("Les trois derniers mots sont {}".format(chaine[length-3:]))



