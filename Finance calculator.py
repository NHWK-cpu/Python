import os
import time

def calculate_finance(pendapatan_perbulan: float, persentase_pajak: float, currency: str) -> None:
    # Perbulan
    pajak_perbulan: float = pendapatan_perbulan * (persentase_pajak/100)
    gaji_bersih_perbulan: float = pendapatan_perbulan - pajak_perbulan

    # Pertahun
    pendapatan_pertahun: float = pendapatan_perbulan * 12
    pajak_pertahun: float = pajak_perbulan * 12
    gaji_bersih_pertahun: float = pendapatan_pertahun - pajak_pertahun

    print('~'*25)
    print(f'Gaji kotor perbulan: {currency} {pendapatan_perbulan:,.0f}')
    print(f'Persentase pajak: {persentase_pajak:,.0f}%')
    print(f'Pajak perbulan: {currency} {pajak_perbulan:,.0f}')
    print(f'Gaji bersih perbulan: {currency} {gaji_bersih_perbulan:,.0f}')

    print('-'*10)

    print(f'Gaji kotor pertahun: {currency} {pendapatan_pertahun:,.0f}')
    print(f'Pajak pertahun: {currency} {pajak_pertahun:,.0f}')
    print(f'Gaji bersih pertahun: {currency} {gaji_bersih_pertahun:,.0f}')
    print('~'*25)

def main() -> None:
    while True:
        try:
            gaji: float = float(input('Masukkan gaji kotor anda: '))
            pajak: float = float(input('Masukkan persentase pajak yang anda tanggung: '))
            currency:str = input('Masukkan mata uang anda: ')
            
            os.system('cls')

            calculate_finance(gaji,pajak,currency)
            
            repeat = input('Apakah anda ingin mengulangi? (y/n) ')
            os.system('cls')
            if repeat == 'n':
                break
        except:
            print('Anda harus memasukkan data dengan benar!')
            time.sleep(2)
            os.system('cls')
            continue

if __name__ == "__main__":
    main()