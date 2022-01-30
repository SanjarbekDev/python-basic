from random import shuffle
names=['Soxibov',"Abrorov","Javohirov","Asilbekov","Elmurodov","Shoxruxov","Jamshidov","Nodirov"]
bilet=[i for i in range(1,len(names))]
shuffle(bilet)
c=-1
for i in names:
    print(f"ism:{i} bilet:{bilet[c]}")
    c=c+1