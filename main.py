from model.daftar_nilai import ubah_data, hapus_data, cari_data
from view.input_nilai import input_nilai

print(" ------------------------------------------------- ")
print("|     APLIKASI PENGOLAHAN DATA NILAI MAHASISWA    |")
print(" ------------------------------------------------- ")
print("| NAMA     : SITI NUR FAUZIAH                     |")
print("| NIM      : 312010032                            |")
print("| KELAS    : TI.20.B.1                            |")
print(" ------------------------------------------------- ")
while True:
    print("MENU : \n 1. Tambah Data \n 2. Ubah Data \n 3. Hapus Data \n 4. Cari Data \n 5. Keluar Aplikasi")
    pilih = int(input("Pilih Menu (1/2/3/4/5) :  "))
    if pilih == 1:
        input_nilai()
    elif pilih == 2:
        ubah_data()
    elif pilih == 3:
        hapus_data()
    elif pilih == 4:
        cari_data()
    elif pilih == 5:
        print("========== ANDA KELUAR DARI APLIKASI ==========")
        break
    else:
        print("!!! === ERROR! Anda Memasukkan Pilihan yang Salah === !!!")