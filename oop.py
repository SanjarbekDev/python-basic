#first oop programming

class Telefon:
    def __init__(self,product_name,RAM,storage,display,OS_version) -> None:
        self.product_name=product_name
        self.RAM=RAM
        self.storage=storage
        self.display=display
        self.OS_version=OS_version

    def get_info(self):
        return f"{self.product_name},{self.RAM},{self.storage},{self.display},{self.OS_version}"
    
    def get_name(self):
        return self.product_name

    def set_version(self,version):
        self.OS_version=version 

iphone6=Telefon("IPHONE 6","2 GB","64 GB","retina",15.1)
print(iphone6.get_name())
iphone6.set_version(15.2)
print(iphone6.get_info())