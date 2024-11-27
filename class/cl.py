class Talaba:
    def __int__(self, name, last_name, year, login, email):
        self.login = login
        self.name = name
        self.last_name = last_name
        self.year = year
        self.email = email
        
    def get_info(self):
        return (f"Foydalanuvchi {self.login}ning ismi : {self.name} {self.last_name}. Tugilgan yili {self.year}.emaili {self.email}")
    
    
    
user1 = Talaba('Jaxongir', 'Abdirimov', 1998, 'abdirimoof4214', 'abdirimoof4214@gmail.com')
print(user1.name)