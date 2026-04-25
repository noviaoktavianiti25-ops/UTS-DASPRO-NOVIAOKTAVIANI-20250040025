def input_mahasiswa():
    nama = input("Nama mahasiswa: ")
    umur = int(input("Umur: "))
    ipk = float(input("IPK: "))
    return nama, umur, ipk

def tampilkan_data(nama, umur, ipk):
    print("\n=== Data Mahasiswa ===")
    print(f"Nama : {nama}")
    print(f"Umur : {umur} tahun")
    print(f"IPK  : {ipk:.2f}")

nama, umur, ipk = input_mahasiswa()
tampilkan_data(nama, umur, ipk)