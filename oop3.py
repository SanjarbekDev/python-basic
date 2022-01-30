from see_methods import see_methods as dir

class Avto:
    def __init__(self,model,rang,narx) -> None:
        self.model=model
        self.rang=rang
        self.narx=narx
        self.kilometr=0

    def get_info(self):
        return f'{self.model},{self.rang},{self.narx},{self.kilometr}km'

    def update_k(self,kilometr):
        if kilometr>0:
            self.kilometr=kilometr
        else:
            print('kamaytirish mumkin emas')

class avtosalon:
    def __init__(self,name,map) -> None:
        self.name=name
        self.map=map
        self.a_soni=0
        self.avto_ship=[]

    def add_avto(self,avto):
        self.avto_ship.append(avto)
        self.a_soni+=1

    def see_avtos(self):
        return [i.get_info() for i in self.avto_ship]





malibu=Avto("Chevrolet malibu","Mokri","30000$")
ravon=Avto("chevrolet nexia3","oq","7000$")
kobalt=Avto('chevrolet kobalt','qora','6000$')

sanjarek_avto=avtosalon("SanjarbekAvto","Navoiy viloyati")
Kamronbek_avto=avtosalon("KamronbekAvto","Navoiy viloyati")
sanjarek_avto.add_avto(malibu)
sanjarek_avto.add_avto(ravon)
sanjarek_avto.add_avto(kobalt)



# print(malibu.get_info())
malibu.update_k(800)
# print(malibu.get_info())
# print(malibu.__kilometr)
print(sanjarek_avto.see_avtos())
print(sanjarek_avto.a_soni)

print(dir(sanjarek_avto))