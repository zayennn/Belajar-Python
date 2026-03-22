def input_data() :
    nilai_siswas = []
    
    jumlah_input_nilai = int(input("masukan jumlah input nilai : "))

    for i in range(jumlah_input_nilai) :
        nilai = int(input(f"masukan nilai ke {i + 1} : "))
        nilai_siswas.append(nilai)
        
    return nilai_siswas

def hitung_rata_rata(nilai_siswas) :
    return sum(nilai_siswas) / len(nilai_siswas)

def tampilkan_data(nilai_siswas, rata_rata) :
    print("\n=============== Data Nilai ===============")

    for i, v in enumerate(nilai_siswas, start=1) :
        print(f"nilai {i} : {v}")

    print(f"nilai rata rata : {rata_rata}")
    
    
nilai_siswas = input_data()
rata_rata = hitung_rata_rata(nilai_siswas)
tampilkan_data(nilai_siswas, rata_rata)