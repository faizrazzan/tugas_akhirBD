import mysql.connector
from Models import makanan_model

# Create mysql connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_makanan"
)


class MakananView:
    def __init__(self):
        self.connection = connection
        self.model = makanan_model.MakananModel()
        pass

    def display(self):
        while True:
            print("1. Insert")
            print("2. Update")
            print("3. Delete")
            print("4. Show")
            print("5. Back")
            match(int(input("Pilih menu: "))):
                case 1:
                    self._insert()
                case 2:
                    self._update()
                case 3:
                    self._delete()
                case 4:
                    self._show()
                case 5:
                    return
                case _:
                    print("Menu tidak tersedia")

    def _insert(self):
        id_jenisMakanan = input("ID Jenis Makanan: ")
        nama_makanan = input("Nama Makanan: ")
        harga_makanan = input("Harga Makanan: ")
        stok_Makanan = input("Stok Makanan: ")  #TODO: Ganti tipedata
        data = (id_jenisMakanan,nama_makanan,harga_makanan,stok_Makanan)
        self.model.insert(data)

    def _update(self):
        id = int(input("ID Makanan: "))
        id_jenisMakanan = int(input("ID Jenis Makanan: "))
        nama_makanan = input("Nama Makanan: ")
        harga_makanan = float(input("Harga Makanan: "))
        stok_makanan = int(input("Stok Makanan: "))
        data = (id_jenisMakanan, nama_makanan, harga_makanan, stok_makanan, id)
        self.model.update(data)

    def _delete(self):
        id_makanan = int(input("ID Makanan: "))
        self.model.delete(id_makanan)

    def _show(self):
        for data in self.model.get_data():
            print("{}. |{} | {} | {} | {} |".format(data[0], data[1], data[2], data[3],data[4]))