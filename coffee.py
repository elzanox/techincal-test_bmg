import tkinter as tk
from PIL import Image, ImageTk
# Daftar menu dan harga
menu = {
    "Produk A": 10000,
    "Produk B": 20000,
    "Produk C": 30000,
    "Produk D": 40000,
    "Produk E": 50000
}

class MenuSelection:
    def __init__(self, master):
        self.master = master
        master.title("Pemilihan Menu Produk")

        # Label instruksi
        self.instructions = tk.Label(master, text="Silakan pilih menu produk:")
        self.instructions.pack()

        # Listbox menu
        self.menu_listbox = tk.Listbox(master)
        for product in menu:
            self.menu_listbox.insert(tk.END, product + " (Rp" + str(menu[product]) + ")")
        self.menu_listbox.pack()

        # Tombol pilih
        self.select_button = tk.Button(master, text="Pilih", command=self.select_product)
        self.select_button.pack()

        # Tombol keluar
        self.quit_button = tk.Button(master, text="Keluar", command=master.quit)
        self.quit_button.pack()

    # Fungsi untuk menampilkan pesan status setelah pemilihan menu produk
    def select_product(self):
        selected_product = self.menu_listbox.get(tk.ACTIVE)
        selected_product = selected_product.split(" (")[0]
        if selected_product not in menu:
            self.status_message.set("Maaf, produk yang Anda pilih tidak tersedia.")
            return
        self.master.withdraw()
        payment_window = tk.Toplevel(self.master)
        payment_window.title("Pembayaran")
        Payment(payment_window, selected_product, menu[selected_product])

class Payment:
    def __init__(self, master, product_name, product_price):
        self.master = master
        self.product_name = product_name
        self.product_price = product_price
        # master.title("Scan untuk Bayar")
        # Label instruksi
        self.instructions = tk.Label(master, text="Konfirmasi Nominal yang sudah anda Transfer:")
        self.instructions.pack()

        # Entry untuk jumlah uang yang dimasukkan
        self.amount_entry = tk.Entry(master)
        self.amount_entry.pack()


           # Gambar barcode
        barcode_image = Image.open("barcode.png")
        barcode_image = barcode_image.resize((250, 300), Image.ANTIALIAS)
        barcode_photo = ImageTk.PhotoImage(barcode_image)
        self.barcode_label = tk.Label(master, image=barcode_photo)
        self.barcode_label.image = barcode_photo  # Simpan referensi agar tidak terhapus oleh garbage collector
        self.barcode_label.pack()
        
        # Tombol bayar
        self.pay_button = tk.Button(master, text="Bayar", command=self.pay)
        self.pay_button.pack()

        # Tombol keluar
        self.quit_button = tk.Button(master, text="Keluar", command=master.quit)
        self.quit_button.pack()

        # Label status pembayaran
        self.status_message = tk.StringVar()
        self.status = tk.Label(master, textvariable=self.status_message)
        self.status.pack()

    # Fungsi untuk memproses pembayaran dan menampilkan pesan status
    def pay(self):
        try:
            amount = int(self.amount_entry.get())
        except ValueError:
            self.status_message.set("Maaf, jumlah uang yang dimasukkan tidak valid.")
            return
        if amount < self.product_price:
            self.status_message.set("Maaf, jumlah uang yang Anda masukkan kurang.")
        else:
            self.status_message.set("Terima kasih! Pembayaran: Rp" + str(amount) + " berhasil")
        self.pay_button.config(state=tk.DISABLED)
        self.amount_entry.config(state=tk.DISABLED)

root = tk.Tk()
app = MenuSelection(root)
root.mainloop()
