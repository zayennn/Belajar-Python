nama = input("masukan nama anda : ")
umur = int(input("masukan umur anda : "))
status = ""

if umur <= 13 :
    print(f"""
nama    : {nama}
umur    : {umur}
status  : anak anak
        """)
elif umur <= 17 :
        print(f"""
nama    : {nama}
umur    : {umur}
status  : remaja
        """)
else : 
        print(f"""
nama    : {nama}
umur    : {umur}
status  : dewasa
        """)