# Addition
def addtion(n=45):
    result = 5 + n
    return result


def multiply():
    result = 5 * 8
    return result


def get_message():
    return "Le résultat du calcul: "


print(get_message(), addtion())
print(get_message(), addtion(4))
print(get_message(), addtion(9))

print(get_message(), multiply())
