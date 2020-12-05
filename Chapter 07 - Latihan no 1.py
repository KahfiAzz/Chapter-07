NamaFile = input('Masukan nama file : ')
try:
 file = open(NamaFile, "r")
 print('Isi file', NamaFile, 'adalah : ')
 print(file.read())
except FileNotFoundError:
 print('File tidak ditemukan')
