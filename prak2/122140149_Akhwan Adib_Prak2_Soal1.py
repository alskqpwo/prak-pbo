class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.__angkatan = angkatan
        self.__isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def mahasiswa_baru(self):
        if self.__isMahasiswa == True:
            if self.__angkatan > 2022:
                return "Mahasiswa baru"
            else:
                return "Bukan mahasiswa baru"
        else :
            return "Bukan mahasiswa"

    def cek_status(self):
        if self.__isMahasiswa:
            return f"{self.__nama} dengan NIM {self.__nim} adalah mahasiswa."
        else:
            return f"{self.__nama} dengan NIM {self.__nim} bukan mahasiswa."

    def perkenalan_diri(self):
        return f"Perkenalkan nama saya {self.__nama} dengan nim {self.__nim} dari angakatan {self.angkatan}"
        

mahasiswa1 = Mahasiswa("201234", "Farhan", 2020)
print(mahasiswa1.cek_status())


mahasiswa2 = Mahasiswa("237890", "Dimas", 2023)
print(mahasiswa2.cek_status())

print(f"\nPerkenalan Mahasiswa 1 Nama: {mahasiswa1.get_nama()}, NIM = {mahasiswa1.get_nim()}")
print(f"Perkenalan Mahasiswa 2 Nama: {mahasiswa2.get_nama()}, NIM = {mahasiswa2.get_nim()}")

print(f"\nApakah Mahasiswa 1 MABA? : {mahasiswa1.mahasiswa_baru()}")
print(f"Apakah Mahasiswa 2 MABA? : {mahasiswa2.mahasiswa_baru()}")

mahasiswa1.set_nama("Yudi")
mahasiswa1.set_nim("184567")
print("\nsetelah diubah")
print(f"\nMahasiswa 1 : {mahasiswa1.get_nama()}, NIM = {mahasiswa1.get_nim()}")
print(f"Mahasiswa 2 : {mahasiswa2.get_nama()}, NIM = {mahasiswa2.get_nim()}")
