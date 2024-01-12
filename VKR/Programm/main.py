# from forms import *
from BD import *

# show()

class Main:

    def autorization(self, login: str, password: str):
        """ Авторизация в систему """
    
        auth =  Autorization()
        if auth.check_login(login):
            if auth.get_password() == password:
                return True # Доступ в систему разрешен

        return False # Доступ в систему запрещен
        

r = Registration()
print(r.registration("Администратор"))

# m = Main()
# mm = m.autorization('Ivan', '12345678')

# print(mm)