import mysql.connector


class TrxModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="db_makanan"
        )

    def get_data(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM transaksi"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def reduce_stock(self, data):
        cursor = self.connection.cursor()
        query = "UPDATE makanan SET STOK_MAKANAN = STOK_MAKANAN - {} WHERE ID_MAKANAN = {}".format(data[1], data[0])
        cursor.execute(query)
        print(cursor.statement)
        self.connection.commit()

    def insert(self, data):
        cursor = self.connection.cursor()
        query = "INSERT INTO transaksi (TGL_PESAN, TOTAL_PEMBAYARAN, JUMLAH_PESANAN) VALUES (NOW(), {}, '{}')".format(
            data[0], data[1])
        cursor.execute(query)
        self.connection.commit()

    def insert_detail(self, data):
        cursor = self.connection.cursor()
        query = "INSERT INTO mengelola (ID_TRANSAKSI, ID_MAKANAN, qty) VALUES ({}, {}, {})".format(data[0],
                                                                                                          data[1],
                                                                                                          data[2])
        cursor.execute(query)
        self.connection.commit()


    def detail_transaksi(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM daftartransaksi"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
