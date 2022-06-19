from views import jenis_view
from views import makanan_view
from views import transaction_view


class MenuView:
    def __init__(self):
        self.jenisView = jenis_view.JenisMakananView()
        self.makananView = makanan_view.MakananView()
        self.transactionView = transaction_view.TransactionView()

    def menu(self):
        while True:
            print("")
            print("Menu")
            print("1. Jenis Makanan")
            print("2. Makanan")
            print("3. Transaksi")
            print("4. Detail Transaksi")
            match int(input("Masukkan Pilihan Anda : ")):
                case 1:
                    self.jenisView.display()
                case 2:
                    self.makananView.display()
                case 3:
                    self.transactionView.buy()
                case 4:
                    self.transactionView.detail()
                case _:
                    print("Masukkan Tidak Benar")
