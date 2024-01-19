from .bd_connect import BdConnect
from .bd_add_data import Bd_add

class First_login:
    ''' добавляет все необходимое при первом запуске программы, когда еще нет пользователей'''

    def is_first_login(self):

        requestString = f'''
        SELECT *
        FROM [Ychpo].[dbo].[polz]
        '''
        
        connect = BdConnect()
        connect.connect()

        dbCursor = connect.conn.cursor()

        dbCursor.execute(requestString)
        result_set = dbCursor.fetchall()

        connect.conn.commit()
        connect.disconnect()

        result = [i for i in result_set]
        if result:
            return False
        else:
            return  True

    def first_login(self, F_P: str, I_P: str, O_P: str, email: str, login: str, password: str):

        add_data = Bd_add()
        add_data.add_polz(F_P, I_P, O_P, email, login, password)
        add_data.add_role("admin", 1, 1, 1, 1)
        add_data.add_dolj("Администратор",1)
        add_data.add_sovm_polz_dolj(1,1)

        add_data.add_role("teacher",  1, 1, 0, 1)
        add_data.add_dolj("Преподаватель", 2)
        add_data.add_role("student", 0, 0, 0, 1)
        add_data.add_dolj("Студент", 3)


# a = First_login()
# a.first_login("Акаков", "Акакий", "Вениаминович","jhgfu@rfj","admin","123")
# # print(a.first_login())