import sqlite3

class Account():
    def __init__(self,database) -> None:
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
    def account_exists(self,user_name,password)->bool:
        with self.connection:
            result = self.cursor.execute("select * from 'players' where  user_name=? and password=?",(user_name,password)).fetchall()
            return bool(len(result))
    def get_info(self,column,user_name):
        with self.connection:
            return self.cursor.execute(f"select {column} from 'players' where user_name= ?",(user_name,)).fetchone()[0]
    def add_account(self,user_name,password):
        with self.connection:
            return self.cursor.execute("insert into 'players' ('user_name','password') values(?,?)",(user_name,password))
    def check_for_name_exists(self,user_name)->bool:
        with self.connection:
            result = self.cursor.execute("select * from 'players' where user_name= ?",(user_name,)).fetchall()
            return bool(len(result))
    def update_info(self,column,data,user_name):
        with self.connection:
            self.cursor.execute(f"update 'players' set {column} = ? where user_name = ?",(data,user_name,))
    def get_best_players(self)->list:
        with self.connection:
            return self.cursor.execute("select * from 'players' order by money DESC").fetchall()
    def close(self):
        self.connection.close()