import mysql.connector


class MakananModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="crystal",
            database="db_makanan"
        )

    def get_data(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM makanan"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def insert(self, data):
        cursor = self.connection.cursor()
        query = "INSERT INTO makanan (nama_makanan, id_jenis_makanan) VALUES ('{}', {})".format(data[0], data[1])
        cursor.execute(query)
        self.connection.commit()

    def update(self, id, data):
        cursor = self.connection.cursor()
        query = "UPDATE makanan SET NAMA_MAKANAN='{}', ID_JENIS_MAKANAN={} WHERE ID_MAKANAN={}".format(data[0], data[1], id)
        cursor.execute(query)
        self.connection.commit()
