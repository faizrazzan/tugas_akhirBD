from Models import jenis_makanan_model


class JenisMakananView:
    def __init__(self):
        self.model = jenis_makanan_model.JenisMakananModel()
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
        for data in self.model.get_data():
            print("{}. {}".format(data[0], data[1]))

