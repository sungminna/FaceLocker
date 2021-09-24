import sqlite3
import pandas as pd

class Db:
    def __init__(self):
        super().__init__()

        self.conn = sqlite3.connect("face.db")
        self.cur = self.conn.cursor()


    def save_user(self):
        pass

    def get_user(self):
        pass

    def get_password(self):
        pass