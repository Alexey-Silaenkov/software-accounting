from .bd_add_data import Bd_add
from .module_autorization import Autorization
from .bd_connect import BdConnect
from .shifr import Crypt




class Registration:

    crypt = Crypt()

    def bd(self, requestString):
        connect = BdConnect()
        connect.connect()

        dbCursor = connect.conn.cursor()

        dbCursor.execute(requestString)
        result_set = dbCursor.fetchall()

        connect.conn.commit()
        connect.disconnect()
        return result_set

    def get_last_id(self, table: str):
      
        requestString = f'''
        SELECT COUNT(*) 
        FROM [Ychpo].[dbo].[{table}]
        '''

        result_set = self.bd(requestString)


        return int(str(result_set[0]).replace("(",'').replace(")",'').replace(",",'')) + 1


    def get_dolj_id(self, name: str):

        name = self.crypt.encrypt(name)

        requestString = f'''
        SELECT [id_dolj]
        FROM [Ychpo].[dbo].[dolj]
        where naim_dolj = '{name}'
        '''

        result_set = self.bd(requestString)

        return int(str(result_set[0]).replace("(",'').replace(")",'').replace(",",''))


    def registration(self, F_P, I_P, O_P, email, login, password,  dolj: str):

        aut = Autorization()
        bd_add = Bd_add()

    
        if not aut.check_login(login):
            bd_add.add_polz( F_P, I_P, O_P, email, login, password)
            bd_add.add_sovm_polz_dolj(aut.get_id(login), self.get_dolj_id(dolj))
            # bd_add.add_sovm_polz_dolj(self.get_last_id("polz")-1, self.get_dolj_id(dolj))
            print(aut.get_id(login))
 
