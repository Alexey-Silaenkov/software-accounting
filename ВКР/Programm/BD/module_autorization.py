from bd_connect import BdConnect
from shifr import Crypt

class Autorization:
    ''' модуль предназначен для вывода информации по определенному пользователю из базы данных '''

    crypt = Crypt()
    
    def check_login(self, login: str):
        
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

        return [i for i in result_set[0]]

    def get_id(self, login: str):  
        return self.check_login(login)[0]

    def get_password(self, login: str):  
        return self.crypt.decrypt(self.check_login(login)[1])

    def get_dostup(self, login: str):  
        return self.check_login(login)[2]
        

# a =  Autorization()
# print(a.get_id('Ivan'))