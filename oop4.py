from enum import auto


class Auto:
    num_auto=0
    def __init__(self,model,narx) -> None:
        self.model=model
        self.narx=narx
        Auto.num_auto+=1

    def __eq__(self,x):
        return self.narx==x.narx

    def __lt__(self,x):
        return self.narx<x.narx

    def __le__(self,x):
        return self.narx<=x.narx

    @classmethod
    def get_num(cls):
        return f"number:{cls.num_auto}"

class avtosalon(Auto):
    def __init__(self, model, narx,manzil) -> None:
        super().__init__(model, narx)
        self.manzil=manzil
        self.avtolist=[]
    
    def add_avto(self,avto):
        self.avtolist.append(avto)


auto1=Auto("gentra",2000)
auto2=Auto("malibu",2000)

# print(auto1==auto2)

# print("Rost" if auto1<=auto2 else "Yolg'on")
nexia=avtosalon("nexia 3",2000,"navoiy viloyati")
nexia.add_avto(auto1)
print(nexia.avtolist)

print(Auto.get_num())




