"""
Connects to a SQL database using pyodbc
"""

import pyodbc

class BdConnect:
    conn = ""
    # Подключение к базе черездрайвер ODBC
    def connect(self):
        self.conn = pyodbc.connect(
            """DRIVER=SQL Server Native Client 11.0;
            DATABASE=Ychpo;
            Trusted_Connection=Yes;
            SERVER=DESKTOP-H7TURC8\SQLEXPRESS """
        )
        print("open")

    # def get_connect(self):
    #     return self.conn

    def disconnect(self): 
        print("close")
        self.conn.close()


