nama_siswa = []
nilai_siswa = []

jumlah_siswa = int(input("masukan jumlah siswa : "))

for i in range(jumlah_siswa) :
    nama = input(f"masukan nama siswa ke - {i} : ")
    nilai = int(input(f"masukan nilai siswa ke - {i} : "))
    
    nama_siswa += nama[i]
    nilai_siswa += nilai[i]
    
print("================ DAFTAR SISWA ================")
for i in range(jumlah_siswa) :
    print(f"""
nama    : {nama_siswa[i]}
nilai   : {nilai_siswa[i]}

===========================

          """)