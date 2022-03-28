a = 'abc'
b = 'bdbcba'
newlist = []
new_a = list(a)
new_b = list(b)
lengh_b = len(new_b)
d = 0
lista2 = []
while lengh_b >= 1:
    for i in new_a:
        for j in new_b:
            if i == j:
                newlist.append(j)
                x = j.index(j)
                new_b.pop(x)
                lengh_b = len(new_b)

            else:
                lista2.append(j)

print(newlist)
print(lista2)
print(lengh_b)






