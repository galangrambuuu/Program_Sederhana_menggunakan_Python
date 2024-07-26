#Rumus BBI: Berat badan ideal dihitung dengan mengurangi 10% (untuk laki-laki) 
# atau 15% (untuk perempuan) dari tinggi badan setelah dikurangi 100.
def cek_bbi():
    print("\n1. Perempuan")
    print("2. Laki-laki")

    gender = 0
    while gender not in [1, 2]:
        gender = int(input("Masukkan kode gender [1/2]: "))
        if gender not in [1, 2]:
            print("Kode yang anda masukkan salah! Silakan coba lagi.")
    
    tinggi_badan = int(input("Masukkan tinggi badan (cm): ")) - 100

    if gender == 1:
        print("\nAnda memilih Perempuan")
        bbi = tinggi_badan - (tinggi_badan * 0.15)
    elif gender == 2:
        print("\nAnda memilih Laki-laki")
        bbi = tinggi_badan - (tinggi_badan * 0.10)
    
    print(f"BBI anda: {bbi:.2f} kg")

#BMI Body Mass Index dihitung dengan membagi berat badan dalam kilogram dengan kuadrat tinggi badan dalam meter.
def cek_bb_normal():
    print("\n1. Perempuan")
    print("2. Laki-laki")

    gender = 0
    while gender not in [1, 2]:
        gender = int(input("Masukkan kode gender [1/2]: "))
        if gender not in [1, 2]:
            print("Kode yang anda masukkan salah! Silakan coba lagi.")

    berat_badan = int(input("Masukkan berat badan (kg): "))
    tinggi_badan = int(input("Masukkan tinggi badan (cm): ")) / 100  # Mengubah tinggi ke meter
    bmi = berat_badan / (tinggi_badan * tinggi_badan)
    print(f"{berat_badan} kg / ({tinggi_badan:.2f} m * {tinggi_badan:.2f} m) = {bmi:.2f}")

    if bmi < 17:
        print("Berat Badan Anda Terlalu Kurus")
    elif 17 <= bmi < 18:
        print("Berat Badan Anda Kurus")
    elif 18 <= bmi < 25:
        print("Berat Badan Anda Normal")
    elif 25 <= bmi < 27:
        print("Berat Badan Anda Gemuk")
    else:
        print("Berat Badan Anda Terlalu Gemuk")

def main():
    print("***********************")
    print("MENGHITUNG BERAT BADAN")
    print("***********************")

    nama = input("Masukkan nama anda: ")
    while nama == "":
        nama = input("Nama tidak boleh kosong. Isi dulu nama anda: ")

    print(f"Halo {nama}, selamat datang!")
    
    while True:
        print("\nMenu:")
        print("1. Cek BBI (Berat Badan Ideal)")
        print("2. Cek BB Normal (BMI)")
        print("3. Keluar")

        cek = 0
        while cek not in [1, 2, 3]:
            cek = int(input("Masukkan pilihan yang ingin anda cek [1/2/3]: "))
            if cek not in [1, 2, 3]:
                print("Kode yang anda masukkan salah! Silakan coba lagi.")

        if cek == 1:
            cek_bbi()
        elif cek == 2:
            cek_bb_normal()
        elif cek == 3:
            print("Anda keluar dari program")
            break
        
        lagi = ''
        while lagi.lower() not in ['y', 'n']:
            lagi = input("Apakah Anda ingin melakukan perhitungan lain? (y/n): ")
            if lagi.lower() not in ['y', 'n']:
                print("Input yang anda masukkan salah! Silakan coba lagi.")

        if lagi.lower() != 'y':
            print("Terima kasih telah menggunakan program!")
            break

if __name__ == "__main__":
    main()
