from operator import itemgetter
book={
    'name':["Python asoslari","Data structures","C++ asoslari"],
    "a_name":["Anvar Narzullayev","Soxibjon Maxmedov","Qudrat abdurahimov"],
    'count':[56,7,32]
}

for i in range(3):
    print(f"Kitob nomi:{book['name'][i]} , muallif {book['a_name'][i]} , Soni: {book['count'][i]} ta")

book["count"][0]=55

for i in range(3):
    print(f"Kitob nomi:{book['name'][i]} , muallif {book['a_name'][i]} , Soni: {book['count'][i]} ta")

