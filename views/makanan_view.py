import mysql.connector

# Create mysql connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="crystal",
    database="db_makanan"
)


class MakananView:
    def __init__(self):
        self.connection = connection
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
        nama_makanan = input("Nama Makanan: ")
        id_jenis = int(input("ID Jenis: "))
        self.model.insert(nama_makanan, id_jenis)

    def _update(self):
        id_makanan = int(input("ID Makanan: "))
        nama_makanan = input("Nama Makanan: ")
        self.model.update(id_makanan, nama_makanan)