from .bd_connect import BdConnect
from .shifr import Crypt

class Autorization:
    ''' модуль предназначен для вывода информации по определенному пользователю из базы данных '''

    login = ""
    crypt = Crypt()
    
    def get_login(self, login: str):
        
        login = self.crypt.encrypt(login)

        requestString = f'''
        SELECT [id_polz]
        ,[password]
        ,[dostup]
        FROM [Ychpo].[dbo].[polz]
        where login = '{login}'
        '''
        
        connect = BdConnect()
        connect.connect()

        dbCursor = connect.conn.cursor()

        dbCursor.execute(requestString)
        result_set = dbCursor.fetchall()

        connect.conn.commit()
        connect.disconnect()

        return result_set

    def check_login(self, login: str):

        result_set = self.get_login(login)

        if result_set:
            self.login = login
            return [i for i in result_set[0]]
        else:
            return False


    def get_id(self):  
        return self.check_login(self.login)[0]

    def get_id(self, login):  
        return self.get_login(login)[0][0]

    def get_password(self):  
        return self.crypt.decrypt(self.check_login(self.login)[1])

    def get_dostup(self):  
        return self.check_login(self.login)[2]
        

# a =  Autorization()
# if a.check_login('Ivan'):
#     print(a.get_dostup())