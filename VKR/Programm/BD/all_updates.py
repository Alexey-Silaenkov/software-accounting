from .bd_connect import BdConnect


class Update_bd:

    def all_edit_func(self, requestString):
        '''Основной алгоритм отправки запросов в бд'''

        connect = BdConnect()
        connect.connect()

        dbCursor = connect.conn.cursor()

        dbCursor.execute(requestString)

        connect.conn.commit()
        connect.disconnect()
        