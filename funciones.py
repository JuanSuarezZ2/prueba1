import psycopg2
import json
import random
import numpy as np


class BD:

    def __init__(self):
        self.con = psycopg2.connect(
            database="enlcuxzb",
            user="enlcuxzb",
            password="bUgzbxegz3BGkRNfRPqvY8y-XpAjy8Mj",
            host="ziggy.db.elephantsql.com",
            port="5432"
    )
    


    def verTienda(self):

        cursor = self.con.cursor()
        query = "select * from mueble where stock != 0"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()
        mensaje = "existe"
        a = {'data': [rows],'mensaje': mensaje}
        return a


