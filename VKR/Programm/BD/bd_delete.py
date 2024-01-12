from .all_updates import Update_bd

class Bd_delete:


    def delete_error(self, id_error: int):
        ''' Удаление данных об ошибке'''

        requestString = f'''
        EXEC error_delete 
        @id_error = {id_error}
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def delete_error(self, id_po: int):
        ''' Удаление данных об ошибке'''

        requestString = f'''
        EXEC po_delete 
        @id_po = {id_po}
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)



# a = Bd_delete()
# a.delete_error(2)