def pilih_menu(menu, pilihan_harga):
    print(f"\n---------- Menu {menu} ----------\n")
    for i, (item, harga) in enumerate(pilihan_harga.items(), 1):
        dots = "-" * (20 - len(item))
        print(f"{i}. {item} {dots} Rp{harga:,}")
    print("\n\033[3m*tolong masukkan nomor pilihan anda!\033[0m")

    nomor = int(input(f"\nMasukkan Pilihan {menu}: "))
    jumlah = int(input(f"\nBerapa {'Porsi' if menu == 'Makanan' else 'Gelas'}: "))

    if 1 <= nomor <= len(pilihan_harga):
        item_pilih = list(pilihan_harga.keys())[nomor - 1]
        total_harga = jumlah * pilihan_harga[item_pilih]
        print(f"{jumlah} {item_pilih} = Rp{total_harga}")
        return item_pilih, total_harga, jumlah
    else:
        print("Pilihan tidak ada, silakan masukkan kembali!")
        return pilih_menu(menu, pilihan_harga)


menu_makanan = {
    "Bakso" : 10000,
    "Mie Ayam" : 13000,
    "Mie Ayam Bakso" : 15000,
    "Soto" : 12000,
    "Nasi Goreng" : 15000,
    "Kwetiau" : 12000,
    "Pangsit" : 12000
}

menu_minuman = {
    "Air Mineral" : 3000,
    "Es Teh Manis" : 4000,
    "Teh Manis Hangat/Panas" : 3000,
    "Es Jeruk" : 6000,
    "Jeruk Hangat/Panas" : 5000,
    "Es Buah" : 8000,
    "Es Cappuccino" : 12000,
    "Capuccino Hangat/Panas" : 11000
}

print("\n---------- Simple Coding --------------")
pembeli = input("\nMasukkan nama Pembeli: ")
print("Nama Pembeli:", pembeli)

mkn, totalmkn, porsi = pilih_menu("Makanan", menu_makanan)
mnm, totalmnm, gelas = pilih_menu("Minuman", menu_minuman)

totalsemua = totalmkn + totalmnm
print("\nTotal Pembayaran: Rp", totalsemua)
uang = int(input("Uang Pembayaran: Rp"))
kembalian = uang - totalsemua
print("Kembalian: ", kembalian)

print("\n===========================================")
print("=============  S T R U K   B E L I ========")
print("===========================================")
print(f"Nama\t\t: {pembeli}")
print(f"Beli\t\t: {porsi} {mkn:<12} (Rp{totalmkn})")
print(f"\t\t\t  {gelas} {mnm:<12} (Rp{totalmnm})")
print(f"Tagihan\t\t: Rp{totalsemua}")
print(f"Dibayar\t\t: Rp{uang}")
print(f"Kembalian\t: Rp{kembalian}")
print("===========================================")
print("===========================================")