class Dagangan:
    jumlah_barang = 0
    list_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((nama, stok, harga))
    
    @classmethod    
    def liat_barang(self):
        print(f"jumlah barang dagangan pada toko: {self.jumlah_barang} buah")
        for i, barang in enumerate(self.list_barang, start=1):
            nama, stok, harga = barang
            print(f"{i}. {nama} seharga Rp {harga} (stok: {stok})")
    
    def __del__(self):
        Dagangan.jumlah_barang -= 1
        for i, barang in enumerate(Dagangan.list_barang):
            if barang[0] == self.__nama:
                del Dagangan.list_barang[i]
                break

Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.liat_barang()
print(f"\n{Dagangan1._Dagangan__nama} dihapus dari toko!")
del Dagangan1

Dagangan.liat_barang()

print(f"\n{Dagangan2._Dagangan__nama} dihapus dari toko!")
del Dagangan2

print(f"\n{Dagangan3._Dagangan__nama} dihapus dari toko!")
del Dagangan3
