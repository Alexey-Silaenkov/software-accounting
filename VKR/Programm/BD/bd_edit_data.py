from .all_updates import Update_bd
from .shifr import Crypt

class Bd_edit:

    crypt = Crypt()

    def edit_error(self, id_error: int, naim_error: str, opisanie: str, sposobYstranenia: str):
        ''' Изменение данных об ошибке'''

        requestString = f'''
        EXEC error_update 
        @id_error = {id_error}, 
        @naim_error = {naim_error}, 
        @opisanie = {opisanie}, 
        @statusError = 1, 
        @sposobYstranenia = {sposobYstranenia}
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def edit_polz(self, id_polz: int, F_P: str, I_P: str, O_P: str, email: str, login: str):
        ''' Изменение данных о пользователе'''

        F_P = self.crypt.encrypt(F_P)
        I_P = self.crypt.encrypt(I_P)
        O_P = self.crypt.encrypt(O_P)
        email = self.crypt.encrypt(email)
        login = self.crypt.encrypt(login)

        requestString = f'''
        EXEC polz_edit 
        @id_polz = '{id_polz}', 
        @F_P = '{F_P}', 
        @I_P = '{I_P}', 
        @O_P = '{O_P}', 
        @email = '{email}', 
        @login = '{login}'
        '''
        update_bd = Update_bd()
        return update_bd.all_edit_func(requestString)


    def edit_polz_full(self, id_polz: int, F_P: str, I_P: str, O_P: str, email: str, login: str, password: str):
        ''' Изменение всех данных о пользователе, в том числе и пароль'''

        requestString = f'''
        EXEC fullpolz_edit 
        @id_polz = {id_polz}, 
        @F_P = {F_P}, 
        @I_P = {I_P}, 
        @O_P = {O_P}, 
        @email = {email}, 
        @login = {login},
        @password = {password}
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def edit_polz_password(self, id_polz: int, password: str):
        ''' Изменение пароля пользователя'''

        requestString = f'''
        EXEC polzpass_edit 
        @id_polz ={id_polz},
        @password = "{password}"
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def edit_zayavka(self, id_zayavkast: int, status: str):
        ''' Изменение данных о заявке'''

        requestString = f'''
        EXEC zayavkast_edit 
        @id_zayavkast = '{id_zayavkast}',
        @status = '{status}'
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def edit_lickluch(self, id_lickluch: int, time: str, date: str, statuskluch: bool):
        ''' Изменение данных об используемом лицензионном ключе'''

        requestString = f'''
        EXEC lickluchtd_edit 
        @id_lickluch = '{id_lickluch}',
        @time = '{time}',
        @date = '{date}',
        @statuskluch = '{statuskluch}'
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)
    

    def edit_po(self, id_PO: int, naim_po:str, kol_po: int, vers_po: str):
        ''' Изменение данных о программном обеспечении'''

        naim_po = self.crypt.encrypt(naim_po)
        vers_po = self.crypt.encrypt(vers_po)

        requestString = f'''
        EXEC po_update 
        @id_PO = '{id_PO}',
        @naim_po = '{naim_po}',
        @kol_po = '{kol_po}',
        @vers_po = '{vers_po}'
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def edit_kol_po(self, id_PO: int, kol_po: int):
        ''' Изменение данных о количестве лицензионных ключей'''

        requestString = f'''
        EXEC pokol_update 
        @id_PO = '{id_PO}',
        @kol_po = '{kol_po}'
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def edit_kluch(self, id_lickluch: int, kod: str):
        ''' Изменение данных о лицензионном ключе'''

        requestString = f'''
        EXEC kluch_edit 
        @id_lickluch = '{id_lickluch}',
        @kod = '{kod}'
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


# dc = Bd_edit()
# dc.edit_error(1,"1","1","1")


