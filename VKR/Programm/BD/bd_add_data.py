from .all_updates import Update_bd
# from .bd_connect import BdConnect
from .shifr import Crypt

class Bd_add:

    crypt = Crypt()



    def add_error(self, naim_error: str, opisanie: str, sposobYstranenia: str):
        ''' Добавление данных об ошибке'''

        naim_error = self.crypt.encrypt(naim_error)
        opisanie = self.crypt.encrypt(opisanie)
        sposobYstranenia = self.crypt.encrypt(sposobYstranenia)


        requestString = f'''
        EXEC error_add 
        @naim_error = {naim_error}, 
        @opisanie = {opisanie}, 
        @statusError = 1, 
        @sposobYstranenia = {sposobYstranenia}
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def add_polz(self, F_P: str, I_P: str, O_P: str, email: str, login: str, password: str):
        ''' Добавление данных о пользователе'''

        F_P = self.crypt.encrypt(F_P)
        I_P = self.crypt.encrypt(I_P)
        O_P = self.crypt.encrypt(O_P)
        email = self.crypt.encrypt(email)
        login = self.crypt.encrypt(login)
        password = self.crypt.encrypt(password)
        

        requestString = f'''
        EXEC polz_add 
        @F_P = '{F_P}', 
        @I_P = '{I_P}', 
        @O_P = '{O_P}', 
        @email = '{email}', 
        @login = '{login}', 
        @password = '{password}', 
        @dostup = 1
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def add_kluch(self, kod: str, statuskluch: bool, pol_id: int):
        ''' Добавление данных о лицензионном ключе'''

        kod = self.crypt.encrypt(kod)

        requestString = f'''
        EXEC kluch_add 
        @kod = {kod},
        @statuskluch ={statuskluch},
        @pol_id = {pol_id}
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def add_po(self, naim_po: str, kol_po: int, vers_po: str):
        ''' Добавление данных о программном обеспечении'''

        naim_po = self.crypt.encrypt(naim_po)
        vers_po = self.crypt.encrypt(vers_po)

        requestString = f'''
        EXEC po_add 
        @naim_po = {naim_po},
        @kol_po = {kol_po},
        @vers_po = {vers_po}
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def add_zayavka(self, status: str, poz_id: int, polz_id: int):
        ''' Добавление данных о заявке обеспечении'''

        requestString = f'''
        EXEC zayavka_add 
        @status = {status},
        @poz_id = {poz_id},
        @polz_id = {polz_id}
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def add_dolj(self, naim_dolj: str, role_id: int):
        ''' Добавление данных о должности'''

        naim_dolj = self.crypt.encrypt(naim_dolj)

        requestString = f'''
        EXEC dolj_add 
        @naim_dolj = '{naim_dolj}',
        @role_id = {role_id}
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def add_sovm_polz_dolj(self, polzsovm_id: int, dolj_id: int):
        ''' Добавление данных о таблице совместимости'''

        requestString = f'''
        EXEC sovm_add 
        @polzsovm_id = {polzsovm_id},
        @dolj_id = {dolj_id}
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def add_sovmosh_polz_error(self, polzsovmosh_id: int, error_id: int):
        ''' Добавление данных о таблице совместимости'''

        requestString = f'''
        EXEC sovmosh_add 
        @polzsovmosh_id = {polzsovmosh_id},
        @error_id = {error_id}
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)


    def add_role(self, naim_role: str, polz_role: bool, zayavka_role: bool, po_role: bool, zakaz_role: bool):
        ''' Добавление данных о роли'''

        naim_role = self.crypt.encrypt(naim_role)

        requestString = f'''
        EXEC role_add 
        @naim_role = '{naim_role}',
        @polz_role = {polz_role},
        @zayavka_role ={zayavka_role},
        @po_role = {po_role},
        @zakaz_role = {zakaz_role}
        '''
        update_bd = Update_bd()
        update_bd.all_edit_func(requestString)



# bd_addd = Bd_add()
# bd_addd.add_polz("Ivanov", "ivan","ivanovich", "123@adfresf","Ivan","12345678")
# bd_addd.add_polz("Фыв", "csd", "vf", "ghgfhdf", "dfg", "dhtdgh")
