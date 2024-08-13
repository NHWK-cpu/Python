from os import *
import time

daftar = []
ops = 10

def main_menu():
    print('Pilih apa yang ingin anda lakukan:')
    print('1. Lihat list yang ada')
    print('2. Tambahkan list')
    print('3. Ubah list')
    print('4. Hapus list')
    print('0. Keluar')

def view_list() -> int:
    '''untuk melihat data'''

    for i in range(len(daftar)): # jika ada data di dalam list
        print(f'{i+1}. {daftar[i]}')
    if len(daftar) == 0: # jika tidak ada data di dalam list
        print('there is no data yet')

    print('-'*15)
    print('9. Kembali ke menu')
    print('0. Keluar')
    return int(input('masukkan perintah: '))

def tambah_daftar() -> int:
    '''untuk menambah data list'''

    while True:
        daftar.append(input('Masukkan catatan: '))
        print('-'*15)
        print('2. Tambahkan lagi data')
        print('9. Kembali ke menu')
        print('0. Keluar')
        return int(input('masukkan perintah: '))

def ubah() ->int:
    '''untuk mengubah data list'''


    # mengecek apakah dalam daftar sudah ada data atau belum
    if len(daftar) == 0: 
        print('Maaf anda belum mempunyai daftar catatan untuk di-edit')
        time.sleep(3)
        system('cls')
        return 9
    else:
        for i in range(len(daftar)): # Memperlihatkan isi list
            print(f'{i+1}. {daftar[i]}')
        print('-'*15)

        # menentukan dan mengubah isi list
        x = int(input('Tentukan catatan nomor berapa yang ingin di-edit? '))
        daftar[x-1] = input('Masukkan catatan baru: ')
        system('cls')

        print('Data telah berhasil diubah!')
        time.sleep(2)
        system('cls')
        return 9

def hapus() -> int:
    '''untuk menghapus data list'''

    if len(daftar) == 0: 
        print('Daftar catatan anda sudah bersih')
        time.sleep(3)
        system('cls')
        return 9
    else:
        for i in range(len(daftar)): # Memperlihatkan isi list
            print(f'{i+1}. {daftar[i]}')
        print('-'*15)
            
        x = int(input('Tentukan catatan nomor berapa yang ingin anda hapus: '))
        del daftar[x-1]

        system('cls')
        for i in range(len(daftar)): # Memperlihatkan isi list
            print(f'{i+1}. {daftar[i]}')
        print('-'*15)

        print('4. Hapus catatan lagi')
        print('9. Kembali ke menu')
        print('0. Keluar')
        return int(input('Masukkan perintah: '))
            

print('Selamat datang!')

while True:
    if ops == 0:
        print("Thanks for using this app!")
        time.sleep(1)
        system('cls')
        break
    elif ops == 1:
        ops = view_list()
        system('cls')
    elif ops == 2:
        ops = tambah_daftar()
        system('cls')
    elif ops == 3:
        ops = ubah()
    elif ops == 4:
        ops = hapus()
        system('cls')
    
    main_menu()
    ops = int(input('masukkan perintah: '))
    system("cls")