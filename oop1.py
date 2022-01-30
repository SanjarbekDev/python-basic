
class Person:
    def __init__(self,ism,familiya,email,parol):
        self.ism=ism
        self.familiya=familiya
        self.email=email
        self.parol=parol
    
    def get_name(self):
        return self.ism

    def get_email(self):
        return self.email

    def get_info(self):
        return f"Foydalanuvchi ismi:{self.ism},familiyasi:{self.familiya},pochta manzili:{self.email}"

    def edit_name(self,newname):
        self.ism=newname

    def edit_email(self,newemail):
        self.email=newemail


user1=Person("Sanjarbek","Sodiqov","umail.com","qwertyui")
user2=Person("Kamronbek","Abdumajidov","jjh.com","qwtsgj111")
# print(user1.get_name())
# print(user1.get_email())
# user1.set_name("SanjarbekDev")
# print(user1.get_name())
print(user2.get_info())
user2.edit_email("kamron.com")
print(user2.get_info())