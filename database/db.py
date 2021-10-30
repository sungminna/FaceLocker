import sqlite3
import pandas as pd

import comparison.compare


class Db:
    def __init__(self):
        super().__init__()

        self.conn = sqlite3.connect("face.db")
        self.cur = self.conn.cursor()



    def save_user_multi(self, table_name, data):    #not in use
        table_name = "u_" + table_name
        text = str()
        for i in range(468):
            text = text + "coord_" + str(i) + " text, "

        text = text[:-2]
        query = "CREATE TABLE IF NOT EXISTS " + table_name + "(" + text + ")"
        self.cur.execute(query)
        self.conn.commit()
        # add user
        # data has faces
        # one line one face
        face_list = list()
        face_tup = tuple()
        for face in data:
            addtext = str()
            for xyz in face:
                s_coord = str(xyz[0]) + '_' + str(xyz[1]) + '_' + str(xyz[2])
                addtext = addtext + s_coord + ", "
            addtext = addtext[:-2]
            tuptext = tuple(map(str, addtext.split(', ')))
            face_list.append(tuptext)
            face_tup = tuple(face_list)

        names = str()
        for i in range(468):
            names += "coord_" + str(i) + ", "
        names = names[:-2]

        qstr = str()
        for i in range(468):
            qstr += "?, "
        qstr = qstr[:-2]
        query = "INSERT INTO " + table_name + "(" + names + ")" + " VALUES(" + qstr + ")"
        self.cur.executemany(query, face_tup)
        self.conn.commit()

    def save_user1(self, id, data):
        table_name = "u_" + id
        text = "x real, y real, z real"

        query = "CREATE TABLE IF NOT EXISTS " + table_name + "(" + text + ")"
        self.cur.execute(query)
        self.conn.commit()
        # add user
        # data has one face

        col_name = ['x', 'y', 'z']
        list_df = pd.DataFrame(data, columns=col_name)
        list_df.to_sql(table_name, self.conn, if_exists='replace')
        self.conn.commit()

    def get_user(self, logger_list):
        col_name = ['x', 'y', 'z']
        logger_df = pd.DataFrame(logger_list, columns=col_name)
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_list = self.cur.fetchall()

        for table in table_list:
            table_name = table[0]

            query = "SELECT * FROM " + table_name
            res = self.cur.execute(query)
            face_data = res.fetchall()
            col_name = ['index', 'x', 'y', 'z']
            list_df = pd.DataFrame(data=face_data, columns=col_name)
            list_df = list_df.drop(columns='index')
            cmp = comparison.compare.Compare()
            result = cmp.compare_user(list_df, logger_df)

            if result == 1:
                print(table_name)
                return(table_name)
            else:
                return(0)



class Passdb:
    def __init__(self):
        super().__init__()

        self.conn = sqlite3.connect("password.db")
        self.cur = self.conn.cursor()

    def add_user(self, id):
        table_name = "u_" + id

        text = "site text, id text, pass text"

        query = "CREATE TABLE IF NOT EXISTS " + table_name + "(" + text + ")"
        self.cur.execute(query)
        self.conn.commit()


    def get_password(self, table_name):
        query = "SELECT * FROM " + table_name
        res = self.cur.execute(query)
        pass_data = res.fetchall()
        col_name = ['site', 'id', 'password']
        pass_df = pd.DataFrame(data=pass_data, columns=col_name)
        return(pass_df, table_name)

    def update_password(self, pass_list, table_name):
        col_name = ['site', 'id', 'password']
        pass_df = pd.DataFrame(pass_list, columns=col_name)
        print(pass_df)
        print(table_name)
        pass_df.to_sql(table_name, self.conn, if_exists='replace')
        self.conn.commit()




if __name__ == '__main__':
    dd = Db()
    pdb = Passdb()