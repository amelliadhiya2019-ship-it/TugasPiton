# 1. Superclass Karyawan
class Karyawan:
    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self._gaji_pokok = gaji_pokok  # Atribut Private (Encapsulation)

    # Getter Gaji Pokok
    def get_gaji_pokok(self):
        return self._gaji_pokok

    # Setter Gaji Pokok dengan validasi
    def set_gaji_pokok(self, gaji_baru):
        if gaji_baru <= 0:
            print(f"[Peringatan] Gaji pokok untuk {self.nama} tidak valid! Harus lebih dari 0.")
        else:
            self._gaji_pokok = gaji_baru
            print(f"[Sukses] Gaji pokok {self.nama} berhasil diubah menjadi: {self._gaji_pokok}")

    def hitung_gaji_total(self):
        return self._gaji_pokok

    def tampilkan_info(self):
        print(f"ID Karyawan : {self.id_karyawan}")
        print(f"Nama        : {self.nama}")
        print(f"Gaji Pokok  : {self._gaji_pokok}")


# 2. Child Class: Karyawan Tetap (Inheritance)
class KaryawanTetap(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan

    # Overriding method hitung_gaji_total
    def hitung_gaji_total(self):
        return self._gaji_pokok + self.tunjangan

    # Overriding method tampilkan_info
    def tampilkan_info(self):
        print("--- DETAIL KARYAWAN TETAP ---")
        super().tampilkan_info()
        print(f"Tunjangan   : {self.tunjangan}")
        print(f"Gaji Total  : {self.hitung_gaji_total()}")
        print("-" * 30)

    
# 3. Child Class: Karyawan Kontrak (Inheritance)
class KaryawanKontrak(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, jam_lembur, tarif_lembur):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.jam_lembur = jam_lembur
        self.tarif_lembur = tarif_lembur

    # Overriding method hitung_gaji_total
    def hitung_gaji_total(self):
        return self._gaji_pokok + (self.jam_lembur * self.tarif_lembur)

    # Overriding method tampilkan_info
    def tampilkan_info(self):
        print("--- DETAIL KARYAWAN KONTRAK ---")
        super().tampilkan_info()
        print(f"Jam Lembur  : {self.jam_lembur} jam")
        print(f"Tarif Lembur: {self.tarif_lembur}")
        print(f"Gaji Total  : {self.hitung_gaji_total()}")
        print("-" * 30)


# ==========================================
# MAIN PROGRAM (PENGUJIAN KODE)
# ==========================================
if __name__ == "__main__":
    # 1. Buat minimal 1 objek Karyawan Tetap dan 1 objek Karyawan Kontrak[cite: 2]
    emp1 = KaryawanTetap("Bagas", "KT001", 5000000, 1500000)
    emp2 = KaryawanKontrak("Yudi", "KK001", 3500000, 10, 50000)

    # 2. Simpan ke dalam list daftar_karyawan[cite: 2]
    daftar_karyawan = [emp1, emp2]

    # 3. Demonstrasi Polymorphism: Looping method tampilkan_info[cite: 2]
    print("\n=== DEMONSTRASI POLYMORPHISM ===")
    for karyawan in daftar_karyawan:
        karyawan.tampilkan_info()

    # 4. Demonstrasi Encapsulation: Ubah gaji dengan nilai tidak valid & valid[cite: 2]
    print("\n=== DEMONSTRASI ENCAPSULATION ===")
    # Uji nilai tidak valid (<= 0)
    emp1.set_gaji_pokok(-1000000) 
    
    # Uji nilai valid (> 0)
    emp1.set_gaji_pokok(5500000)

    # Tampilkan info terbaru setelah perubahan
    print("\n=== HASIL AKHIR SETELAH PERUBAHAN GAJI ===")
    emp1.tampilkan_info()