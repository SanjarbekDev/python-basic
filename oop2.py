from time import strftime

class shaxs:
    def __init__(self,ism,familiya,tyil) -> None:
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil

    def __repr__(self) -> str:
        return f"Shaxs: {self.ism} {self.familiya} {self.tyil}"

    def get_info(self):
        info=f"ism:{self.ism} familiya:{self.familiya} tug'ulgan yili:{self.tyil}"
        return info

    def get_age(self):
        age=int(strftime('%Y'))-self.tyil
        return age

class Talaba(shaxs):
    def __init__(self,ism,familiya,tyil) -> None:
        super().__init__(ism,familiya,tyil)
        self.bosqich=1
        self.fanlar_soni=0
        self.fanlar=[]

    def get_info(self):
        return f'Talaba:{self.ism} {self.familiya},{self.bosqich} bosqich talabasi'

    def get_fanlar(self):
        return [fan.get_fan() for fan in self.fanlar]

    def set_bosqich(self,bosqich):
        self.bosqich=bosqich

    def fanga_yozil(self,fan):
        self.fanlar.append(fan)
        self.fanlar_soni+=1

    def remove_fan(self,fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            self.fanlar_soni-=1
        else:
            print("Siz bu fanga yozilmagansiz!")


    def update_bosqich(self):
        self.bosqich+=1

class Fan:
    def __init__(self,nomi) -> None:
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]

    def get_fan(self):
        return f"Fan nomi:{self.nomi}, ro'yxatdan o'tgan talabalar:{self.talabalar_soni}"

    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni+=1
    
    def get_student(self):
        return [talaba.get_info() for talaba in self.talabalar]


class Professor(shaxs):
    def __init__(self, ism, familiya, tyil) -> None:
        super().__init__(ism, familiya, tyil)
        self.count_jobs=0
        self.jobs_map=[]

    def set_jobs(self,*args):
        for job in args:
            self.jobs_map.append(job)

    def get_jobs(self):
        for job in self.jobs_map:
            print(job)

talaba1=Talaba("Sanjarbek","Sodiqov",2000)
# talaba2=Talaba("Soxib","Maxmedov",2003)
# talaba3=Talaba("Javohir","Qurbonov",2001)
# MTA=Fan("Malumotlar tuzilmasi")
# kiber=Fan("Kiber Xavfsizlik asoslari")
# fizika=Fan("Fizika")
# print(talaba1.get_info())

# MTA.add_student(talaba2)
# MTA.add_student(talaba3)
# fizika.add_student(talaba1)
# print(MTA.get_student())
# talaba1.fanga_yozil(fizika)
# talaba1.fanga_yozil(MTA)
# talaba1.fanga_yozil(kiber)

# talaba1.remove_fan(MTA)
# print(talaba1.get_fanlar())

professor1=Professor("Sanjarbek","Sodiqov",2000)
# professor1.set_jobs("SamTUIT","Uzdevs GRoup")
# professor1.get_jobs()
print(professor1)



