menu = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Goreng": 18000,
    "Es Teh": 5000,
    "Es Jeruk": 6000,
    "Air Mineral": 3000
}

def tampilkan_menu():
    print("Menu Makanan/Minuman:")
    for item, harga in menu.items():
        print(f"{item}: Rp {harga}")

def hitung_total(hitungan):
    total = sum(hitungan.values())
    return total

def tampilkan_struk(pesanan, total_harga):
    print("\n===== Struk Pembelian =====")
    for item, harga in pesanan.items():
        print(f"{item}: Rp {harga}")
    print(f"Total Harga: Rp {total_harga}")
    print("===========================\n")

def main():
    pesanan = {}
    lanjut = True

    tampilkan_menu()

    while lanjut:
        pilihan = input("Pilih menu (atau ketik 'selesai' untuk selesai): ")
        if pilihan.lower() == 'selesai':
            lanjut = False
        elif pilihan in menu:
            if pilihan in pesanan:
                pesanan[pilihan] += menu[pilihan]
            else:
                pesanan[pilihan] = menu[pilihan]
            print(f"{pilihan} telah ditambahkan ke dalam pesanan.")
        else:
            print("Menu tidak tersedia.")

    total_harga = hitung_total(pesanan)
    tampilkan_struk(pesanan, total_harga)

if __name__ == "__main__":
    main()
