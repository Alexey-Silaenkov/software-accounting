from .bd_connect import BdConnect
import pyodbc


class Update_bd:

    def all_edit_func(self, requestString):
        '''Основной алгоритм отправки запросов в бд'''

        connect = BdConnect()
        connect.connect()

        dbCursor = connect.conn.cursor()
        try:
            dbCursor.execute(requestString)
        except pyodbc.Error as e:
            return e
        connect.conn.commit()
        connect.disconnect()
        