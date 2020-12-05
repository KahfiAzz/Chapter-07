NamaFile = input('Masukan nama file : ')
try:
 while True:
     file = open(NamaFile, "a")
     data = input('Data yang mau ditambahkan : ')
     file.write(data + "\n")
     file.close()
     print('Ulangi lagi (y/n)? : ')
     jawab = input()
     if jawab == 'n':
        break

 file = open(NamaFile, "r")
 print('Isi file', NamaFile, 'setelah ditambahkan adalah : ')
 print(file.read())
except FileNotFoundError:
 print('File tidak ditemukan')
