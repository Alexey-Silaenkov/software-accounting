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

        # print(result_set)
        # print(result_set[0])
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

    def get_polz_view_not_admin(self, dolj = "Администратор"):

        dolj = self.crypt.encrypt(dolj)

        requestString = f'''
        SELECT *
        FROM [Ychpo].[dbo].[polzv]
        where [Должность] != '{dolj}'
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

    def get_zayavki_view(self):

        requestString = f'''
        SELECT *
        FROM [Ychpo].[dbo].[zayavki_view]
       
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
                    result_user.append(self.crypt.decrypt(k))
                except:
                    result_user.append(k)
            result_users.append(result_user)
            result_user = []

        # print(result_users)
        
                    

        return result_users


    def get_po_view(self):

        requestString = f'''
        SELECT *
        FROM [Ychpo].[dbo].[PO]
       
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
        
                    

        return result_users


    def get_po_zayavki_view(self):

        requestString = f'''
        SELECT *
        FROM [Ychpo].[dbo].[PO]
        where [kol_po] > 0
       
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
        
                    

        return result_users


    def get_self_keys_view(self, login):

        login = self.crypt.encrypt(login)

        requestString = f'''
        SELECT *
        FROM [Ychpo].[dbo].[statistika]
        where [Логин] = '{login}'
       
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
            if result_user not in result_users:
                result_users.append(result_user)
            result_user = []
        
                    

        return result_users


    def get_dostup(self, login):

        login = self.crypt.encrypt(login)

        requestString = f'''
        SELECT [Доступ к заявкам],
        [Доступ к пользователям],
        [Доступ к ПО],
        [Доступ к заказам]
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
            

        result = []
        key = []
        for item in result_set:
            for k in item:
                try:
                    key.append(self.crypt.decrypt(k))
                except:
                    key.append(k)
            result.append(key)
            key = []
            

        return result[0]


    def get_fio(self, login):

        login = self.crypt.encrypt(login)

        requestString = f'''
        SELECT [Фамилия пользователя],
        [Имя пользователя],
        [Очество пользователя]
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

        result = []
        for i in range(len(result_set[0])):
            fio = self.crypt.decrypt(str(result_set[0][i]).replace("(",'').replace(")",'').replace(",",''))
            result.append(fio)
            
        # print(result)
        # print(result_set)


        return result


    def get_role(self, login):

        login = self.crypt.encrypt(login)

        requestString = f'''
        SELECT [Должность]
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
        # print(result_set)

        role = self.crypt.decrypt(str(result_set[0]).replace("(",'').replace(")",'').replace(",",'').replace("'",''))
        return role


    def get_keys(self, id_po):


        requestString = f'''
        SELECT [kod],
        [id_lickluch]
        FROM [Ychpo].[dbo].[lickluch]
        where [pol_id] = '{id_po}'
        '''
        
        connect = BdConnect()
        connect.connect()

        dbCursor = connect.conn.cursor()

        dbCursor.execute(requestString)
        result_set = dbCursor.fetchall()

        connect.conn.commit()
        connect.disconnect()

        result = []
        key = []
        for item in result_set:
            for k in item:
                try:
                    key.append(self.crypt.decrypt(k))
                except:
                    key.append(k)
            result.append(key)
            key = []
            

        return result


    def get_code(self, name, version):

        crypt = Crypt()

        name = crypt.encrypt(name)
        version = crypt.encrypt(version)

        requestString = f'''
        SELECT *
        FROM [Ychpo].[dbo].[izmlickluch]
        where [Название ПО] = '{name}' and [Версия] = '{version}' and [Доступен] = 1
        '''
        
        
        connect = BdConnect()
        connect.connect()

        dbCursor = connect.conn.cursor()

        dbCursor.execute(requestString)
        result_set = dbCursor.fetchall()

        connect.conn.commit()
        connect.disconnect()

        result = []
        key = []
        for item in result_set:
            for k in item:
                try:
                    key.append(self.crypt.decrypt(k))
                except:
                    key.append(k)
            result.append(key)
            key = []
        

        return result[0]        



    def get_statistic(self):

        crypt = Crypt()

        requestString = f'''
        SELECT *
        FROM [Ychpo].[dbo].[statistika]
        '''
        
        
        connect = BdConnect()
        connect.connect()

        dbCursor = connect.conn.cursor()

        dbCursor.execute(requestString)
        result_set = dbCursor.fetchall()

        connect.conn.commit()
        connect.disconnect()

        result = []
        key = []
        for item in result_set:
            for k in item:
                try:
                    key.append(self.crypt.decrypt(k))
                except:
                    key.append(k)
            if key not in result:
                result.append(key)
            key = []
        

        return result    