
def addition():
    result=5+5
    return result


def multipliy():
    result=5*8
    return result

def get_msg():
    return  "Le  resultat est : "

def test(x):
    result=x+5
    return result

print(get_msg() , addition())
print("Le  resultat est : " , multipliy())
print(get_msg() , test(5))