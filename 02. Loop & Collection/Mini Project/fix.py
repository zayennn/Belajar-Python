data_siswa = []

jumlah_siswa = int(input("masukan jumlah siswa : "))

total_nilai = 0

for i in range(jumlah_siswa) :
    print(f"\n================ input siswa ke - {i} ================\n")
    nama = input("masukan nama siswa : ")
    nilai = int(input("masukan nilai siswa : "))
    
    siswa = {
        "nama" : nama,
        "nilai" : nilai
    }
    
    data_siswa.append(siswa)
    total_nilai += nilai
    
nilai_rata_rata = total_nilai / jumlah_siswa

print("\n================ DAFTAR SISWA ================")
for siswa in data_siswa :
    print(f"""
===========================
nama    : {siswa["nama"]}
nilai   : {siswa["nilai"]}
===========================""")

print("nilai rata rata siswa adalah : ", nilai_rata_rata)