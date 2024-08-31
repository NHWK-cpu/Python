def calculate_split(total_biaya: float, jumlah_orang: int, mata_uang: str) -> None:
    if jumlah_orang < 1:
        raise ValueError("Jumlah orang harus lebih dari nol!")
    
    if total_biaya < 0:
        raise ValueError("Total tagihan tidak mungkin kurang dari nol!")
    
    pembagian_per_orang: float = total_biaya / jumlah_orang

    print(f'Total biaya: {mata_uang} {total_biaya:,.0f}')
    print(f'Jumlah orang: {jumlah_orang}')
    print(f'Jumlah yang harus dibayarkan per-orang: {mata_uang} {pembagian_per_orang:,.0f}')


def main() -> None:
    try:
        total_tagihan: float = float(input("Masukkan total tagihan: "))
        jumlah_orang: int = int(input("Masukkan jumlah orang yang ikut patungan: "))
        mata_uang: str = input("Masukkan mata uang tagihan anda: ")

        print('-'*25)

        calculate_split(total_tagihan,jumlah_orang,mata_uang)
    except ValueError as message:
        print(f'error: {message}')

if __name__ == "__main__":
    main()