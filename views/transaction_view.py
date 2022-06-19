from Models import transaction_model, makanan_model


class TransactionView:
    def __init__(self):
        self.transaction_model = transaction_model.TrxModel()
        self.makanan_model = makanan_model.MakananModel()

    def show_cart(self, cart_dict):
        """
        Print user cart to screen
        """
        makanan_list = self.makanan_model.get_data()
        for makanan in makanan_list:
            if makanan[0] in cart_dict:
                print("{}. {} (Rp. {} each)".format(makanan[0], makanan[2], makanan[3]))
                print("{} x {}".format(cart_dict[makanan[0]], makanan[3] * cart_dict[makanan[0]]))
                print("=" * 20)

    def buy(self):
        makanan_list = self.makanan_model.get_data()
        cart_dict = {}
        while True:
            print("Select item to buy:")
            for index, makanan in enumerate(makanan_list):
                print("{}. {} (Rp. {} each)".format(index + 1, makanan[2], makanan[3]))
            print("0. Checkout")
            print("{}. Cart".format(len(makanan_list) + 1))
            choice = int(input(">> "))
            if choice == 0:
                print(cart_dict)
                self.check_out(cart_dict)
                break
            elif choice == len(makanan_list) + 1:
                self.show_cart(cart_dict)
            elif 0 < choice <= len(makanan_list):
                print("How many {} do you want to buy?".format(makanan_list[choice - 1][2]))
                qty = int(input(">> "))
                cart_dict[makanan_list[choice - 1][0]] = qty
            else:
                print("Invalid choice")

    def check_out(self, cart_dict):
        makanan_list = self.makanan_model.get_data()
        total_price = 0
        jumlah_pesanan = 0

        for makanan in makanan_list:
            if makanan[0] in cart_dict:
                jumlah_pesanan += cart_dict[makanan[0]]
                total_price += makanan[3] * cart_dict[makanan[0]]

        print("Total price: {}".format(total_price))
        print("Do you want to buy? (y/n)")
        choice = input(">> ")
        if choice == "y":
            self.transaction_model.insert([total_price, jumlah_pesanan])
            for makanan in makanan_list:
                if makanan[0] in cart_dict:
                    self.transaction_model.insert_detail([self.transaction_model.get_data()[-1][0], makanan[0], cart_dict[makanan[0]]])
            print("Thank you for your purchase")
        else:
            print("Thank you")
