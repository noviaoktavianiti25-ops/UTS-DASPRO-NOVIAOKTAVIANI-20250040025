def hitung_kategori(rata_rata):
    if rata_rata >= 0.8:
        return "Produktif Tinggi"
    elif rata_rata >= 0.5:
        return "Produktif Sedang"
    else:
        return "Produktif Rendah"

def program_peternak():
    total_telur = 0

    for hari in range(1, 8):
        print(f"\nHari ke-{hari}")
        
        nama_kandang = input("Nama kandang: ")
        jumlah_ayam = int(input("Jumlah ayam: "))
        jumlah_telur = int(input("Jumlah telur: "))
        
        # Validasi
        if jumlah_ayam == 0:
            print("Jumlah ayam tidak boleh 0!")
            continue
        
        rata_rata = jumlah_telur / jumlah_ayam
        kategori = hitung_kategori(rata_rata)

        total_telur += jumlah_telur

        print(f"Rata-rata telur/ayam: {rata_rata:.2f}")
        print("Kategori:", kategori)

    print("\n=== Laporan 7 Hari ===")
    print("Total produksi telur:", total_telur)

program_peternak()