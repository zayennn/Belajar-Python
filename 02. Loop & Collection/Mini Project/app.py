nama_siswa = []
nilai_siswa = []

jumlah_siswa = int(input("masukan jumlah siswa : "))

total_nilai = 0

for i in range(jumlah_siswa) :
    nama = input(f"masukan nama siswa ke - {i + 1} : ")
    nilai = int(input(f"masukan nilai siswa ke - {i + 1} : "))
    
    nama_siswa.append(nama)
    nilai_siswa.append(nilai)
    
    total_nilai += nilai_siswa[i]
    
print("\n================ DAFTAR SISWA ================")
for i in range(jumlah_siswa) :
    print(f"""
===========================
nama    : {nama_siswa[i]}
nilai   : {nilai_siswa[i]}
===========================""")