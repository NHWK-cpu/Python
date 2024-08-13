import os

os.chdir("D:\Programing learn\Python\PROJECT\database")

count = input('berapa file yang ingin anda tambahkan? ')

while not count.isdigit():
    count = input('tolong masukkan angka! ')

count = int(count)

for i in range(count):
    new_file = input('masukkan nama file: ')

    with open(new_file,'w', encoding='utf-8') as f:
        f.write('')


print('selesai ditambahkan')