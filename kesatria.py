def petualanganKsatria(jarak, lebar_langkah, nyawa_awal):
    langkah = 1
    nyawa = nyawa_awal
    
    print("MULAI", end="  ")

    while langkah <= jarak:
        if langkah % 4 == 0:
            print("JEBAKAN", end="  ")
            nyawa -= 1
            if nyawa == 0:
                print("GAGAL")
                return
        elif langkah % 6 == 0:
            print("NYAWA+", end="  ")
            nyawa += 1
        else:
            print(langkah, end="  ")
        langkah += lebar_langkah
    print("BERHASIL")

# Contoh penggunaan
petualanganKsatria(12, 1, 3)
