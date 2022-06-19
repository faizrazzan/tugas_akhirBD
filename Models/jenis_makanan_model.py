import mysql.connector

# Create mysql connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_makanan"
)


class JenisMakananModel:
    def __init__(self):
        self.connection = connection
        pass

    def get_data(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM jenis_makanan"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def insert(self, data):
        cursor = self.connection.cursor()
        query = "INSERT INTO jenis_makanan (nama_jenis_makanan) VALUES ('{}')".format(data)
        cursor.execute(query)
        self.connection.commit()

    def update(self, id, data):
        cursor = self.connection.cursor()
        query = "UPDATE jenis_makanan SET NAMA_JENIS_MAKANAN='{}' WHERE ID_JENIS_MAKANAN={}".format(data, id)
        cursor.execute(query)
        self.connection.commit()

    def delete(self, id):
        cursor = self.connection.cursor()
        query = "DELETE FROM jenis_makanan WHERE ID_JENIS_MAKANAN={}".format(id)
        cursor.execute(query)
        self.connection.commit()


