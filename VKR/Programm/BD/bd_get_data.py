from .bd_connect import BdConnect
from .shifr import Crypt


class Bd_get_data:

    crypt = Crypt()

    def get_iddolj(self, login):

        login = self.crypt.encrypt(login)

        requestString = f'''
        SELECT [Номер должности]
        FROM [Ychpo].[dbo].[polzv]
        where [Логин] = '{login}'
        '''
        
        connect = BdConnect()
        connect.connect()

        dbCursor = connect.conn.cursor()

        dbCursor.execute(requestString)
        result_set = dbCursor.fetchall()

        connect.conn.commit()
        connect.disconnect()


        return(int(str(result_set[0]).replace("(",'').replace(")",'').replace(",",'')))

    def get_email(self, login):

        login = self.crypt.encrypt(login)

        requestString = f'''
        SELECT [Email]
        FROM [Ychpo].[dbo].[polzv]
        where [Логин] = '{login}'
        '''
        
        connect = BdConnect()
        connect.connect()

        dbCursor = connect.conn.cursor()

        dbCursor.execute(requestString)
        result_set = dbCursor.fetchall()

        connect.conn.commit()
        connect.disconnect()

        user_email = str(result_set[0]).replace("(",'').replace(")",'').replace(",",'')

        # print(self.crypt.decrypt(user_email))

        return(self.crypt.decrypt(user_email))

        # result = [i for i in result_set]
        # if result:
        #     return False
        # else:
        #     return  True


    def get_polz_view(self):

        requestString = f'''
        SELECT *
        FROM [Ychpo].[dbo].[polzv]
       
        '''
        
        connect = BdConnect()
        connect.connect()

        dbCursor = connect.conn.cursor()

        dbCursor.execute(requestString)
        result_set = dbCursor.fetchall()

        connect.conn.commit()
        connect.disconnect()

        crypt = Crypt()
        result_users = []
        result_user = []
        
        for item in result_set:
            for k in item:
                try:
                    result_user.append(crypt.decrypt(k))
                except:
                    result_user.append(k)
            result_users.append(result_user)
            result_user = []

        # print(result_users)
        
                    

        return result_users
        # return(int(str(result_set[0]).replace("(",'').replace(")",'').replace(",",'')))
