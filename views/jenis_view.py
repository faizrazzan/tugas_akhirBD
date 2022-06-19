from Models import jenis_makanan_model
from views import menu_file
from prettytable import PrettyTable


class JenisMakananView:
    def __init__(self):
        self.model = jenis_makanan_model.JenisMakananModel()
        #self.Menu = menu_file.MenuView()

    def display(self):
        while True:
            print("1. Insert")
            print("2. Update")
            print("3. Delete")
            print("4. Show")
            print("5. Back")
            match int(input("Pilih menu: ")):
                case 1:
                    self._insert()
                case 2:
                    self._update()
                case 3:
                    self._delete()
                case 4:
                    self._show()
                case 5:
                    break
                case _:
                    print("Menu tidak tersedia")

    def _insert(self):
        nama_jenis = input("Nama Jenis: ")
        self.model.insert(nama_jenis)

    def _update(self):
        id_jenis = int(input("ID Jenis: "))
        nama_jenis = input("Nama Jenis: ")
        self.model.update(id_jenis, nama_jenis)

    def _delete(self):
        id_jenis = int(input("ID Jenis: "))
        self.model.delete(id_jenis)

    def _show(self):
        x = PrettyTable()
        x.field_names = ["ID Jenis", "Jenis Makanan"]
        for data in self.model.get_data():
            x.add_row(data)
        print(x)



