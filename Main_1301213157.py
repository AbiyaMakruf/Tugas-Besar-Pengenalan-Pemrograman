#Nama   : Muhammad Abiya Makruf
#NIM    : 1301213157
#Kelas  : IF - 45 - 07
#Tugas  : 34. CATUR HULA-HULA



#Deklarasi fungsi
def baca_Data(input_User):
    """    
    Fungsi untuk baca data dari file teks.
    Fungsi digunakan untuk memilih data mana yang akan digunakan

    Jika input dari user bukan angka 1/2/3 fungsi akan mencetak pesan error, dan meminta input kembali dari user
    Jika input sudah sesuai, fungsi akan me-return sebuah file teks yang akan dibaca

    Parameters:
    input_User (string): Pilihan opsi 
    """
    #Perulangan yang digunakan untuk memastikan bahwa input user adalah angka 1/2/3
    #Dan jika input user bukan angka 1/2/3, maka akan mencetak pesan error, dan meminta input kembali
    while input_User != "1" and input_User != "2" and input_User!="3":
        print("Maaf pilihan input tidak tersedia, silahkan input kembali"+"\n") #Mencetak pesan error
        input_User = input("Silahkan pilih file: ") #Meminta input dari user lagi

    #Jika input yang diminta sudah sesuai, kode akan lanjut 
    if input_User == "1": #Jika input=="1", program akan me-return open file dengan file yang diopen adalah "data1.txt"
        return open("data1.txt","r"), input_User
    elif input_User == "2": #Jika input=="2", program akan me-return open file dengan file yang diopen adalah "data2.txt"
        return open("data2.txt","r"), input_User
    elif input_User =="3": #Jika input=="3", program akan me-return open file dengan file yang diopen adalah "data3.txt"
        return open("data3.txt","r"), input_User

def pemilihanFileTeks ():
    """    
    Prosedur yang digunakan untuk mencetak ke layar, ada berapa file teks yang dapat dipilih user
    Prosedur yang digunakan untuk mendapatkan isi file yang sudah di olah


    Parameters:
    Tidak ada parameters yang dibutuhkan.
    
    """
    #Mencetak menu ke layar, dan meminta input dari user
    print("Pilihan data yang tersedia: ")
    print("[1] File teks-1")
    print("[2] File teks-2")
    print("[3] File teks-3")
    input_User = input("Silahkan pilih file: ")

    #Baca data dari teks file.
    isi, input_User = baca_Data(input_User) #Menjalankan fungsi baca_data dengan parameters nya adalah angka yang di input oleh user
    isiFile = isi.read() #Membaca file yang di open menggunakan read()
    isi.close() #Menutup file setelah dibuka dan dibaca

    #Membuat list 
    posisiPapanCatur = isiFile.split("/") #Isi file displit berdasarkan "/", sehingga menjadi sebuah list. Di split berdasarkan "/" karena "/" merupakan tanda yang memberitahu bahwa bagian selanjutnya adalah baris yang berbeda

    #Membuat sebuah list bernama posisi yang isinya adalah pembacaan dari file teks.
    posisi = []
    for elemen in isiFile.replace("/",""): #Me-replace "/"  dengan "", kemudian kita ambil per elemen dari setiap baris, kemudian di append ke dalam list posisi
        posisi.append(elemen)

    #Mencetak isi data kedalam sebuah list, dan mencetak pembacaan dari data tersebut.
    print("\n"+"="*(len(posisi)*5)) #Mencetak garis "===" sebanyak len() dari list posisi kemudian dikali 5
    print("Isi dari file teks-{}".format(input_User).center(len(posisi)*5)) #Mencetak kalimat, dengan format cetakan berada di tengah garis "==="
    print(str(posisi)) #Mencetak list posisi, dengan format cetakan berada di tengah layar
    print(("="*(len(posisi)*5)) +"\n") #Mencetak garis "===" sebanyak len() dari list posisi kemudian dikali 5

    #Me-return beberapa variabel yang diperlukan untuk kebutuhan program
    return (isiFile,posisiPapanCatur,posisi,input_User)

def nilai_buah(posisi,pemain):
    """    
    Fungsi untuk menghitung nilai buah dari pemain catur hitam atau putih

    Parameters:
    poisi (list): List dari posisi pion catur
    pemain (string): String dari pilihan hitam/putih, parameters ini didapatkan dari input user
    """
    
    #Sebuah dictionary dengan key adalah nama pion, dan value adalah nilai dari pion tersebut
    dict_buah_hitam = {"k":200,"q":9,"r":5,"b":3,"n":3,"p":1}
    dict_buah_putih = {"K":200,"Q":9,"R":5,"B":3,"N":3,"P":1}

    #Jika input pemain dari user =="hitam", maka hitung jumlah nilai_buah 
    if pemain == "hitam":
        totalNilaiHitam = 0 #Sebuah variabel untuk menyimpan total nilai
        #Perulangan untuk mengambil huruf dari sebuah list
        #For baris, digunakan untuk mengambil setiap baris
        #For huruf, digunakan untuk mengambil setiap elemen pada baris
        for baris in posisi:
            for huruf in baris:
                if huruf in dict_buah_hitam: #Jika huruf berada pada dictionary, variabel total += nilai dari huruf tersebut
                    totalNilaiHitam += dict_buah_hitam[huruf]
        return totalNilaiHitam #Mengembalikan variabel total untuk buah hitam

    #Jika input pemain dari user =="putih", maka hitung jumlah nilai_buah 
    elif pemain == "putih":
        totalNilaiPutih = 0 #Sebuah variabel untuk menyimpan total nilai
        #Perulangan untuk mengambil huruf dari sebuah list
        #For baris, digunakan untuk mengambil setiap baris
        #For huruf, digunakan untuk mengambil setiap elemen pada baris
        for baris in posisi:
            for huruf in baris:
                if huruf in dict_buah_putih: #Jika huruf berada pada dictionary, variabel total += nilai dari huruf tersebut
                    totalNilaiPutih += dict_buah_putih[huruf]
        return totalNilaiPutih #Mengembalikan variabel total untuk buah putih

def jumlah_petak_kosong(posisi):
    """    
    Fungsi untuk menghitung jumlah petak kosong pada papan

    Parameters:
    poisis (list): List dari posisi pion catur
    """

    #Membuat variabel yang berisi string angka dari 1-8
    listAngka = "12345678"
    totalPetakKosong = 0 #Variabel untuk menyimpan jumlah petak kosong
    #Perulangan untuk mengambil setiap baris satu persatu
    #Perulangan untuk mengambil setiap elemen dari baris
    for baris in posisi:
        for i in baris:
            if i in listAngka: #Jika elemen tersebut adalah sebuah angka, atau elemen tersebut berada di dalam listAngka
                totalPetakKosong+= int(i) #Maka variabel total += elemen tersebut yang sudah diubah kedalam bentuk integer
    return totalPetakKosong #Me return variabel totalPetakKosong

def papanCatur(posisi):
    """    
    Fungsi untuk menampilkan isi data dalam file teks, menjadi visualisasi jika di papan catur
    Ini merupakan fungsi tambahan, bukan merupakan fungsi yang diminta pada tugas

    Parameters:
    poisis (list): List dari posisi pion catur
    """

    print() #Mencetak baris kosong untuk dijadikan jarak
    print("PAPAN CATUR".center(17)) #Mencetak kalimat "PAPAN CATUR", dengan format berapa ditengah-tengah

    #Melakukan pengulangan sebanyak len(posisi)
    for i in range(len(posisi)):
        if len(posisi[i]) != 1: #Jika panjang posisi[i] tidak sama dengan 1, maka jalankan kode dibawah
            for isi in posisi[i]:
                if isi.isdigit(): #Jika elemen ke-i adalah sebuah digit (yaitu angka 1/2/3/4/5/6/7)
                    posisi[i] = posisi[i].replace(isi, "."*int(isi)) #Ubah elemen ke-i tersebut dengan "."
            print("{}{}{}".format("|",(" ").join(posisi[i]),"|")) #Mencetak "|", mencetak baris ke-i ke layar, dan mencetak "|" kembali
        else:
            #Jika panjang posisi[i] adalah 1, maka dapat dipastikan bahwa pada baris tersebut 8 petak kosong semua
            #Sehingga kita dapat langsung mengubahnya menjadi 8 titik kosong
            print("|. . . . . . . .|")
    print() #Mencetak baris kosong untuk dijadikan jarak




#Main program
def mainProgram ():
    #Menjalankan prosedur, prosedur digunakan agar user dapat memilih file teks yang akan digunakan
    #Hasil nya disimpan ke dalam beberapa variabel
    isiFile,posisiPapanCatur,posisi,input_User= pemilihanFileTeks()

    kondisi = True #Ketika kondisi=False, maka program akan terhenti
    #Sebuah pengulangan agar user dapat menjalankan kode terus-menerus sampai user ingin berhenti
    while kondisi:
        
        #Mencetak tampilan menu dari macam-macam fungsi yang dapat digunakan pada program ini.

        # *Menu UTAMA*
        print("Daftar fungsi yang dapat digunakan: " + "\n"
              "[1] Mencari nilai buah pemain." + "\n"
              "[2] Menghitung jumlah petak kosong." + "\n"
              "[3] Mencetak papan catur." + "\n"
              "[4] Ganti file data."+"\n"
              "[5] Untuk exit dari program.")

        #Exception Handling
        #Jika input user bukan berupa angka
        #Program akan memberi tahu, bahwa input harus berupa angka
        #Dan user akan diarahkan kembali ke menu awal (*Menu UTAMA*)
        try:
            #Meminta input dari user, input digunakan untuk memilih menu
            input_User = int(input("Masukkan angka 1/2/3/4/5: "))

            #Jika user memilih 1, maka akan menjalankan fungsi "nilai_buah"
            if input_User == 1:
                #Mencetak opsi ke layar user, untuk memberi pertanyaan, pemain manakah yang ingin dihitung nilai_buah nya
                print("\n"+"1. Menghitung nilai buah pemain buah catur hitam."+"\n"
                      "2. Menghitung nilai buah pemain buah catur putih." )
                #Exception Handling
                #Jika input user bukan berupa angka
                #Program akan memberi tahu, bahwa input harus berupa angka
                #Dan user akan diarahkan kembali ke menu awal (*Menu UTAMA*)
                try:
                    input_User = int(input("Masukkan angka 1/2: ")) #Meminta input dari user
                    if input_User == 1: #Jika input user == 1, maka akan dihitung nilai_buah pemain hitam
                        print("\n"+"Nilai buah pemain catur hitam adalah {}.".format(nilai_buah(posisi,"hitam")))
                        input_Konfirmasi = input("Tekan enter untuk melanjutkan") #Hanya sebuah tambahan, agar user dapat melihat dengan jelas output yang diberikan
                        print()
                    elif input_User == 2: #Jika input user == 1, maka akan dihitung nilai_buah pemain hitam
                        print("\n"+"Nilai buah pemain catur putih adalah {}.".format(nilai_buah(posisi,"putih")))
                        input_Konfirmasi = input("Tekan enter untuk melanjutkan") #Hanya sebuah tambahan, agar user dapat melihat dengan jelas output yang diberikan
                        print()
                    else:
                        #Jika user meng input angka, tetapi angka yang diinput tidak tersedia pada opsi
                        #Program akan memberi tahu bahwa pilihan angka yang diinput tidak terdapat pada opsi
                        print("Maaf pilihan angka tidak terdapat pada opsi."+"\n")
                except:
                    #Exception Handling
                    #Program akan memberi tahu, bahwa input harus berupa angka
                    #Dan user akan diarahkan kembali ke menu awal (*Menu UTAMA*)
                    print("Maaf input salah, input harus berupa angka."+"\n")
                
            #Jika user memilihi 2, maka akan menjalankan fungsi "jumlah_petak_kosong"
            elif input_User == 2:
                print("\n"+"Jumlah petak kosong adalah {}.".format(jumlah_petak_kosong(posisi))) #Menjalankan fungsi "jumlah_petak_kosong"
                input_Konfirmasi = input("Tekan enter untuk melanjutkan") #Hanya sebuah tambahan, agar user dapat melihat dengan jelas output yang diberikan
                print() #Mencetak baris kosong untuk sebuah batas

            #Jika user memilih 3, maka akan menjalankan fungsi "papanCatur", yaitu fungsi yang digunakan untuk mencetak isi dari file teks, menjadi visualisasi jika berapada diatas papan catur
            elif input_User == 3:
                papanCatur(posisiPapanCatur) #Menjalankan fungsi "papanCatur"
                input_Konfirmasi = input("Tekan enter untuk melanjutkan") #Hanya sebuah tambahan, agar user dapat melihat dengan jelas output yang diberikan
                print() #Mencetak baris kosong untuk sebuah batas

            #Jika user memilih 4, makan user akan diarahkan kembali ke menu pertama, yaitu menu agar user dapat memilih file teks mana yang ingin digunakan
            elif input_User == 4:
                print() #Mencetak baris kosong untuk sebuah batas
                isiFile,posisiPapanCatur,posisi,input_User= pemilihanFileTeks() #Menjalankan prosedur untuk memilih file teks

            #Jika user memilih 5, maka akan membuat variabel "kondisi" yang tadinya bernilai True menjadi False, 
            #Sehingga perulangan akan berhenti, dan kode juga akan berhenti berjalan
            elif input_User == 5:
                kondisi = False

            else:
                #Jika user meng input angka, tetapi angka yang diinput tidak tersedia pada opsi
                #Maka program akan mencetak kode ini
                print("Maaf pilihan angka tidak terdapat pada opsi."+"\n")


        except: 
            #Exception Handling
            #Program akan memberi tahu, bahwa input harus berupa angka
            #Dan user akan diarahkan kembali ke menu awal (*Menu UTAMA*)
            print("Maaf input salah, input harus berupa angka."+"\n")




#Menjalankan main program
mainProgram() 

#Setelah code sudah beres, maka akan mencetak "===", dan juga mencetak ucapan terimakasih
print("="*70)   
print("Terima kasih sudah menggunakan program ini.".center(70))

#Program Selesai.