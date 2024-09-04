def persentase_pengeluaran(list_orang: list) -> dict:

    '''fungsi ini digunakan untuk menghitung persentase pengeluaran dari setiap orang (pengguna harus menghitung persentase manual)'''

    orang_dan_tagihannya: dict = {}
    while True:
        persentasi:float = 100
        try:
            for i in list_orang:
                # akan ototmatis mengisi angka 0 jika pembagian persentase sudah mencapai 100
                if persentasi < 1:
                    tagihan: float = 0
                else:
                    tagihan: float = float(input(f'berapa persen tagihan dari {i}: '))
                    persentasi = persentasi - tagihan
                    
                    if tagihan > 100:
                        raise ValueError("Jumlah persentase tidak boleh lebih dari 100%")
                orang_dan_tagihannya.update({i:tagihan})
            break
        except ValueError as message:
            print(f'error: {message}')
    
    return orang_dan_tagihannya

def input_nama_orang(jumlah_orang_yang_ikut:int) -> list:
    '''fungsi ini digunakan untuk memasukkan nama orang-orang yang ikut patungan'''
    list_orang:list = []
    for i in range(jumlah_orang_yang_ikut):
        list_orang.append(input(f'Nama orang ke-{i+1} yang ikut patungan: '))
    return list_orang

def calculate_split(total_biaya: float, jumlah_orang: int, mata_uang: str) -> None:
    if jumlah_orang < 1:
        raise ValueError("Jumlah orang harus lebih dari nol!")
    
    if total_biaya < 0:
        raise ValueError("Total tagihan tidak mungkin kurang dari nol!")
    
    # baris ini digunakan untuk menentukan apakah pengguna ingin membedakan persentase patungan tiap orang
    option = input('(y/n) apakah anda ingin membedakan perorang dengan persentase tagihan yang berbeda? ')
    if option == 'y' or option == 'yes':
        # jika ya, pengguna harus menginput nama orang-orang dan persentase patungan mereka
        list_orang:list = input_nama_orang(jumlah_orang)
        pembagian_per_orang:dict = persentase_pengeluaran(list_orang)
        
        print('-'*25)
        print(f'Total biaya: {mata_uang} {total_biaya:,.0f}')
        print(f'Jumlah orang: {jumlah_orang}')

        for orang in list_orang:
            print(f'Jumlah yang harus dibayarkan {orang}: {mata_uang} {(total_biaya*pembagian_per_orang[orang]/100):,.0f}')
    else:
        pembagian_per_orang: float = total_biaya / jumlah_orang

        print(f'Total biaya: {mata_uang} {total_biaya:,.0f}')
        print(f'Jumlah orang: {jumlah_orang}')
        print(f'Jumlah yang harus dibayarkan per-orang: {mata_uang} {pembagian_per_orang:,.0f}')


def main() -> None:
    # Pengguna akan memasukkan data
    while True:
        try:
            total_tagihan: float = float(input("Masukkan total tagihan: "))
            jumlah_orang: int = int(input("Masukkan jumlah orang yang ikut patungan: "))
            mata_uang: str = input("Masukkan mata uang tagihan anda: ")

            print('-'*25)

            calculate_split(total_tagihan,jumlah_orang,mata_uang)
            break
        except ValueError as message:
            # jika terjadi error selama proses, akan dikeluarkan peringatan error dan menghentikan proses
            print(f'error: {message}')

if __name__ == "__main__":
    main()