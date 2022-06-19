import mysql.connector


class MakananModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
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
        query = "INSERT INTO makanan (id_jenis_makanan,nama_makanan,harga_makanan,stok_makanan) VALUES ('{}','{}',{}," \
                "'{}')".format(
            data[0], data[1], data[2], data[3])
        cursor.execute(query)
        self.connection.commit()

    def update(self, data):
        cursor = self.connection.cursor()
        query = "UPDATE makanan SET ID_JENIS_MAKANAN={},NAMA_MAKANAN='{}',HARGA_MAKANAN={},STOK_MAKANAN={} WHERE " \
                "ID_MAKANAN={}". \
            format(data[0], data[1], data[2], data[3], data[4])
        cursor.execute(query)
        self.connection.commit()
