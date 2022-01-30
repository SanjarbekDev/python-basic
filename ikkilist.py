l1=list(range(1,101))
l2=list(range(2,100))
# l2.append(list(range(50,100)))
# print(l2)
for i in l1:
    if i not in l2:
        print(i)
