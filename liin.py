philips=["Vacuum Cleaner","Straightener","Epilator","Iron","Epilator","Hairdryer","Hair Clipper","Mixer","Garment Steamer"]
bosch=["Straightener","WASHING MACHINE WAT2846XME","Epilator","REFRIGERATOR KGN36NL30U","Straightener","Garment Steamer","Vacuum Cleaner"]
li=[]

for i in philips:
    if i in bosch:
        li.append(i)
print(li)