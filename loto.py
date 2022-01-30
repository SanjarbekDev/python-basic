DATA={
    'city':["Toshkent","Samarqand","Navoi"],
    'count':[56,7,32],
    "name":["Anvar Narzullayev","Soxibjon Maxmedov","Qudrat abdurahimov"],
    "date":[13,5,24]
    
}

for i in range(3):
    print(f"manzil: {DATA['city'][i]}, chipta raqami:{DATA['count'][i]},ismi:{DATA['name'][i]}, sana: {DATA['date'][i]} ")