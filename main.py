from views import jenis_view, transaction_view


if __name__ == '__main__':
    loadView = transaction_view.TransactionView()
    loadView.buy()
