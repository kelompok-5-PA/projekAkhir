from prettytable import PrettyTable
from datetime import datetime
import json
import pwinput
import os

os.system("cls")

class EMoney:
    def __init__(self):
        self.saldo = 0

    def top_up(self, jumlah):
        self.saldo += jumlah
        print(f"Saldo Anda telah ditambahkan sebesar {jumlah} e-money. Saldo sekarang: {self.saldo} e-money.")

    def cek_saldo(self):
        return self.saldo

    def bayar(self, jumlah_bayar):
        if self.saldo >= jumlah_bayar:
            self.saldo -= jumlah_bayar
            print(f"Pembayaran berhasil! Saldo sekarang: {self.saldo} e-money.")
            return True
        else:
            print("Saldo e-money tidak mencukupi. Silakan top up terlebih dahulu.")
            return False

def load_data():
    if os.path.isfile("kain.json"):
        with open("kain.json", "r") as json_file:
            kain_data = json.load(json_file)
            return kain_data["produk_kain"]
    else:
        jenis_kain = [
            [1, "Sutra", 99000, 120],
            [2, "Velvet", 99000, 120],
            [3, "Katun", 82000, 100],
            [4, "Linen", 82000, 100],
            [5, "Organza", 65000, 100],
            [6, "Polyester", 40000, 80],
            [7, "Rajut", 99000, 80]
        ]
        return jenis_kain

def save_data(jenis_kain):
    kain_data = {
        "produk_kain": jenis_kain
    }

    kain_json = json.dumps(kain_data, indent=4)
    with open("kain.json", "w") as json_file:
        json_file.write(kain_json)

def create_produk(jenis_kain):
    nama = input("Masukkan nama produk kain: ")
    harga = int(input("Masukkan harga produk kain: "))
    stok = int(input("Masukkan stok produk kain: "))

    new_produk = [len(jenis_kain) + 1, nama, harga, stok]
    jenis_kain.append(new_produk)
    save_data(jenis_kain)
    print(f"Produk {nama} telah ditambahkan.")

def read_daftarkain(jenis_kain):
    if jenis_kain:
        table = PrettyTable()
        table.field_names = ["No", "Nama", "Harga", "Stok"]
        for index, produk in enumerate(jenis_kain, 1):
            table.add_row([index, produk[1], produk[2], produk[3]])
        print(table)
    else:
        print("Tidak ada produk kain yang tersedia.")

def update_produk(jenis_kain):
    read_daftarkain(jenis_kain)
    try:
        index = int(input("Masukkan nomor produk kain yang akan diperbarui: ")) - 1
        if 0 <= index < len(jenis_kain):
            produk = jenis_kain[index]
            print("Data Produk Saat Ini:")
            print(f"Nama: {produk[1]}, Harga: {produk[2]}, Stok: {produk[3]}")
            new_nama = input("Masukkan nama produk kain baru (kosongkan untuk tidak mengubah): ")
            new_harga = input("Masukkan harga produk kain baru (kosongkan untuk tidak mengubah): ")
            new_stok = input("Masukkan stok produk kain baru (kosongkan untuk tidak mengubah): ")

            if new_nama:
                produk[1] = new_nama
            if new_harga:
                produk[2] = int(new_harga)
            if new_stok:
                produk[3] = int(new_stok)

            save_data(jenis_kain)
            print("Data produk kain berhasil diperbarui.")
        else:
            print("Nomor produk kain tidak valid.")
    except ValueError:
        print("Masukan tidak valid.")

def delete_produk(jenis_kain):
    read_daftarkain(jenis_kain)
    try:
        index = int(input("Masukkan nomor produk kain yang akan dihapus: ")) - 1
        if 0 <= index < len(jenis_kain):
            deleted_produk = jenis_kain.pop(index)
            save_data(jenis_kain)
            print(f"Produk {deleted_produk[1]} telah dihapus.")
        else:
            print("Nomor produk kain tidak valid.")
    except ValueError:
        print("Masukan tidak valid.")

def generate_invoice(customers_name, customer_order, total_bill, payment, change):
    invoice = PrettyTable()
    invoice.field_names = ["Berkain", "Invoice"]
    invoice.add_row(["Nama Pelanggan:", customers_name])
    invoice.add_row(["Waktu Transaksi:", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    for kain, quantity in customer_order.items():
        for produk in jenis_kain:
            if produk[1] == kain:
                price_per_meter = produk[2]
                invoice.add_row([kain, f"{quantity} x Rp. {price_per_meter:.2f}"])

    invoice.add_row(["Total Transaksi:", f"Rp. {total_bill:.2f}"])
    invoice.add_row(["Jumlah Pembayaran:", f"Rp. {payment:.2f}"])
    invoice.add_row(["Kembali:", f"Rp. {change:.2f}"])

    print(invoice)

def checkout(jenis_kain, user_data, saldo_emoney):
    customer_order = {}
    total_bill = 0

    while True:
        print("Daftar Kain Tersedia:")
        read_daftarkain(jenis_kain)
        nomor = int(input("Masukkan nomor produk yang akan dibeli (0 untuk selesai): "))
        if nomor == 0:
            break

        for produk in jenis_kain:
            if int(produk[0]) == nomor:
                jumlah = int(input("Masukkan jumlah produk yang akan dibeli: "))
                if jumlah <= produk[3]:
                    if produk[1] in customer_order:
                        customer_order[produk[1]] += jumlah
                    else:
                        customer_order[produk[1]] = jumlah
                    total_harga = jumlah * produk[2]
                    total_bill += total_harga
                    print(f"Total harga: Rp. {total_harga:.2f}")
                    print("Produk berhasil ditambahkan ke keranjang.")
                    produk[3] -= jumlah
                else:
                    print("Maaf, stok produk tidak mencukupi.")

    customers_name = input("Masukkan nama pelanggan: ")

    print(f"Total belanja Anda adalah: Rp. {total_bill:.2f}")

    print("\nPilih metode pembayaran:")
    print("1. Pembayaran Tunai")
    print("2. Pembayaran dengan E-Money")

    metode_pembayaran = input("Pilih metode pembayaran (1/2): ")

    if metode_pembayaran == '1':
        while True:
            payment = int(input("Masukkan jumlah pembayaran tunai: "))
            if payment >= total_bill:
                change = payment - total_bill
                break
            else:
                print("Jumlah pembayaran kurang dari total belanja. Coba lagi.")
    elif metode_pembayaran == '2':
        if total_bill <= saldo_emoney.cek_saldo():
            change = 0
            saldo_emoney.bayar(total_bill)
        else:
            print("Maaf, saldo e-Money tidak mencukupi untuk pembayaran ini.")
            print(f"Saldo e-Money Anda: Rp {saldo_emoney.cek_saldo():,.2f}")
            print("Silakan isi saldo e-Money Anda terlebih dahulu.")
            return

    generate_invoice(customers_name, customer_order, total_bill, total_bill, change)
    save_user_data("user_data.json", user_data)

def read_user_data(file_name):
    try:
        with open(file_name, 'r') as file:
            user_data = json.load(file)
            if "admins" not in user_data:
                user_data["admins"] = []
            if "customers" not in user_data:
                user_data["customers"] = []
        return user_data
    except FileNotFoundError:
        return {"admins": [], "customers": []}

def save_user_data(file_name, user_data):
    with open(file_name, 'w') as file:
        json.dump(user_data, file, indent=4)

def register(role, user_data):
    print(f"=== Pendaftaran {role.capitalize()} ===")
    username = input("Masukkan username: ")
    password = pwinput.pwinput("Masukkan password: ")

    user_list = user_data.get(f"{role}s", [])
    user_list.append({"username": username, "password": password})

    user_data[f"{role}s"] = user_list
    save_user_data("user_data.json", user_data)

    print(f"{role.capitalize()} {username} telah berhasil terdaftar.\n")

def login(role, user_data):
    print(f"=== Login {role.capitalize()} ===")
    username = input("Masukkan username: ")
    password = pwinput.pwinput("Masukkan password: ")

    user_list = user_data.get(f"{role}s", [])
    for user in user_list:
        if user["username"] == username and user["password"] == password:
            print(f"Welcome {role} {username}! Have a Great Day :)\n")
            return True
    print("Login gagal. Coba lagi.\n")
    return False

def display_user_data(user_data):
    for role in ["admin", "customer"]:
        table = PrettyTable()
        table.field_names = ["Username"]
        user_list = user_data.get(f"{role}s", [])
        for user in user_list:
            table.add_row([user["username"]])
        print(f"{role.capitalize()}s:")
        print(table)
        print()

def initial_emoney():
    print("Selamat datang di E-Money!")
    saldo_awal = 0
    saldo_customer = EMoney()
    saldo_customer.saldo = saldo_awal
    print(f"Saldo Awal e-Money Anda: Rp {saldo_customer.cek_saldo():,.2f}")
    return saldo_customer

def topup_emoney(saldo_customer):
    print("\nPilih nominal top-up E-Money:")
    print("1. Rp 1.000.000")
    print("2. Rp 2.500.000")
    print("3. Rp 6.000.000")
    print("4. Rp 8.000.000")
    print("5. Rp 10.000.000")

    pilihan = input("Pilih nomor opsi top-up: ")

    if pilihan == '1':
        saldo_customer.top_up(1000000)
    elif pilihan == '2':
        saldo_customer.top_up(2500000)
    elif pilihan == '3':
        saldo_customer.top_up(6000000)
    elif pilihan == '4':
        saldo_customer.top_up(8000000)
    elif pilihan == '5':
        saldo_customer.top_up(10000000)
    else:
        print("Pilihan tidak valid. Silakan pilih nomor opsi top-up yang sesuai.")
        return

    print(f"Saldo E-Money Anda sekarang: Rp {saldo_customer.cek_saldo():,.2f}")

def e_money(saldo_customer):
    while True:
        print("\nPilih tindakan e-Money:")
        print("1. Top-up")
        print("2. Cek Saldo")
        print("3. Checkout")
        print("4. Keluar")

        pilihan = input("Silakan Pilih Opsi : ")

        if pilihan == '1':
            topup_emoney(saldo_customer)
        elif pilihan == '2':
            print(f"Saldo Anda saat ini: Rp {saldo_customer.cek_saldo():,.2f}")
        elif pilihan == '3':
            checkout(jenis_kain, user_data, saldo_customer)
        elif pilihan == '4':
            print("Terima kasih")
            return
        else:
            print("Pilihan tidak valid.")

jenis_kain = load_data()
user_data = read_user_data("user_data.json")

def main_menu():
    print("""
+=====================================================+
|              SELAMAT DATANG DI BERKAIN              |
+=====================================================+
""")

    while True:
        print("          |--------- Masuk Sebagai ---------|")
        print("          |---------------------------------|")
        print("          |1.| ADMIN                        |")
        print("          |2.| CUSTOMER                     |")
        print("          |3.| LEAVE                        |")
        print("          |---------------------------------|\n")

        try:
            pilihan = int(input("Masukkan pilihan : "))
            if pilihan == 1:
                admin_menu()
            elif pilihan == 2:
                customer_menu()
            elif pilihan == 3:
                print("""
+====================================+
|                                    |
|       THANK YOU FOR VISITING       |
|           OUR SHOP !! :D           |
|                                    |
+====================================+
""")
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except KeyboardInterrupt:
            print("\nJangan tekan ctrl + c")
        except ValueError:
            print("Oops! Harap masukkan angka. Silahkan coba kembali . . .")

def admin_menu():
    while True:
        print(
        """
        ------------- PILIH LOGIN -------------
        |1.| Registrasi                       |
        |2.| Login                            |
        |3.| Exit                             |
        ---------------------------------------
        """)

        try:
            sub_pilihan = int(input("Masukkan pilihan : "))
            if sub_pilihan == 1:
                register("admin", user_data)
            elif sub_pilihan == 2:
                if login("admin", user_data):
                    admin_actions()
                else:
                    print("Login gagal. Coba lagi.")
            elif sub_pilihan == 3:
                print("""
+===================================+
|                                    |
|       YOU'VE BEEN LOGGED OUT       |
|                                    |
+===================================+
""")
                break  # Keluar dari loop saat exit
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Oops! Harap masukkan angka. Silahkan coba kembali . . .")

def admin_actions():
    while True:
        print("""
+===================================+
|              Pilihan              |
+===================================+
|    1. Create Menu                 |
|    2. Read Menu                   |
|    3. Update Menu                 |
|    4. Delete Menu                 |
|    5. Logout                      |
+===================================+
""")
        try:
            sub_pilihan = int(input("Masukkan pilihan : "))
            if sub_pilihan == 1:
                create_produk(jenis_kain)
            elif sub_pilihan == 2:
                read_daftarkain(jenis_kain)
            elif sub_pilihan == 3:
                update_produk(jenis_kain)
            elif sub_pilihan == 4:
                delete_produk(jenis_kain)
            elif sub_pilihan == 5:
                print("""
+===================================+
|                                    |
|       YOU'VE BEEN LOGGED OUT       |
|                                    |
+===================================+
""")
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Oops! Harap masukkan angka. Silahkan coba kembali . . .")

def customer_menu():
    print(
        """
        ------------- PILIH LOGIN -------------
        |1.| Registrasi                       |
        |2.| Login                            |
        |3.| Exit                             |
        ---------------------------------------
        """
    )
    try:
        sub_pilihan = int(input("Masukkan pilihan : "))
        if sub_pilihan == 1:
            register("customer", user_data)
        elif sub_pilihan == 2:
            if login("customer", user_data):
                customer_actions()
            else:
                print("Login gagal. Coba lagi.")
        elif sub_pilihan == 3:
            print("""
+===================================+
|                                    |
|       YOU'VE BEEN LOGGED OUT       |
|                                    |
+===================================+
""")
            return
        else:
            print("Pilihan tidak valid. Coba lagi.")
    except ValueError:
        print("Oops! Harap masukkan angka. Silahkan coba kembali . . .")

def customer_actions():
        print("""
+===================================+
|              Pilihan              |
+===================================+
|    1. Read Menu                   |
|    2. e-Money                     |
|    3. Logout                      |
+===================================+
""")
        try:
            sub_pilihan = int(input("Masukkan pilihan : "))
            if sub_pilihan == 1:
                read_daftarkain(jenis_kain)
                print("Apakah Anda ingin melanjutkan?")
                lanjut = input("Lanjutkan? (y/n): ")
                if lanjut.lower() != 'n':
                    customer_actions()
            elif sub_pilihan == 2:
                saldo_customer = initial_emoney()
                e_money(saldo_customer)
            elif sub_pilihan == 3:
                print("""
+===================================+
|                                    |
|       YOU'VE BEEN LOGGED OUT       |
|                                    |
+===================================+
""")
                return
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Oops! Harap masukkan angka. Silahkan coba kembali . . .")

if __name__ == "__main__":
    main_menu()
