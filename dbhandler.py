import mysql.connector
import constantes

class DataBasehandler():
    def __init__(self):
        DataBasehandler.HOST = constantes.HOST
        DataBasehandler.USER = constantes.USER
        DataBasehandler.DBNAME = constantes.DATABASE
        DataBasehandler.PASSWORD = constantes.PASS

    HOST = constantes.HOST
    USER = constantes.USER
    DBNAME = constantes.DATABASE
    PASSWORD = constantes.PASS
    @staticmethod

    def get_mydb():
        if DataBasehandler.DBNAME == '':
            constantes.init()

        db = DataBasehandler()
        mydb = db.connect()

        return mydb

    def connect(self):
        mydb = mysql.connector.connect(
            host=DataBasehandler.HOST,
            user=DataBasehandler.USER,
            password=DataBasehandler.PASSWORD,
            database=DataBasehandler.DBNAME
        )

        return mydb