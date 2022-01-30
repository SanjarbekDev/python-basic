# a=["Sanjar","Kamron"]

# print(*a)
# Output : Sanjar Kamron
x={
    'a':1,
    'b':2,
    'c':3
}

def pprint(a,b,c):
    print(a)
    print(b)
    print(c)

pprint(**x)

'''
    Output:
            1
            2
            3
'''