c=[i for i in range(1,10)]
print(c)
for i in c:
    if i%2==0:
        c.remove(i)

print(c)