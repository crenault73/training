import random
import copy

size= 4

def get_elementn(table, n):
    return table[int(n/4)][n%4]

def shuffle_table(table):
    l = random.sample(range(0, 16), 16)
    print ("Random elem l:", l)
    table_tmp = copy.deepcopy(table)
    n = 0
    for i in range(0,4):
        for j in range(0,4):
            table[i][j] = get_elementn(table_tmp,l[n])
            n+=1
    return table

#table =[[4,5,6,7],[8,9,10,11],[12,13,14,15],[0,1,2,3]]
table =[["A","B","C","D"],["E","F","G","H"],["I","J","K","L"],["M","N","O",None]]


print("Table :",table)
print("Table shuffled:",shuffle_table(table))
