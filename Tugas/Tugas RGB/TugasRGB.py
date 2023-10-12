import os
from PIL import Image

def clear():
    # Membersihkan layar konsol
    os.system('cls' if os.name == 'nt' else 'clear')


def Baca():
    # Buka citra
    gambar= input("Input Image dengan Extensinya: ")
    image = Image.open(gambar) 

    # Tentukan koordinat titik yang ingin Anda baca
   # titik koordinat yang ingin di cek
    x = int(input("Input koordinat x: "))
    y = int(input("Input koordinat y: "))

    # Baca nilai RGB dari pixel di titik tertentu
    pixel_color = image.getpixel((x, y))

    # Pisahkan nilai RGB
    red, green, blue = pixel_color

    print(f"Nilai RGB pada titik ({x}, {y}):")
    print(f"Red: {red}")
    print(f"Green: {green}")
    print(f"Blue: {blue}")

def Edit():
    # Buka citra cover image
    image=input("Input Image dengan Extensinya: ")
    citra_cover = Image.open(image)

    # Koordinat titik di mana Anda ingin menulis nilai RGB
    # titik koordinat yang ingin di cek
    x = int(input("Input koordinat x: "))
    y = int(input("Input koordinat y: "))

    # Baca nilai RGB dari pixel di titik tertentu
    pixel_color = citra_cover.getpixel((x, y))

    # Pisahkan nilai RGB
    red, green, blue = pixel_color

    # Nilai RGB yang ingin Anda tulis
    print(f"Nilai RGB yang ingin di rubah pada titik ({x}, {y}):")
    print(f"Red: {red}")
    print(f"Green: {green}")
    print(f"Blue: {blue}")

   # memasukkan warna RGB baru dalam format "R G B" pada titik yang dipilih
    input_warna_baru = input(
        "Masukkan Nilai RGB baru (Contoh, 255 0 0 untuk merah): ")

    # Memecah input RGB baru menjadi tiga komponen warna (R, G, B)
    komponen_warna = input_warna_baru.split()

    # Memastikan ada tiga komponen RGB yang valid
    if len(komponen_warna) == 3:
        red_new, green_new, blue_new = map(int, komponen_warna)

        # Ganti warna di titik yang sama dengan warna baru
        warna_baru = (red_new, green_new, blue_new)
        citra_cover.putpixel((x, y), warna_baru)
    else:
        print("Format warna RGB tidak valid. Harap masukkan tiga komponen Warna (R G B).")
    

    # Simpan citra cover yang telah diperbarui
    nama= input("Berikan Nama Untuk Judul Gambar: ")
    citra_cover.save(nama)

    # Tutup citra
    citra_cover.close()


while True:
    print("PROGRAM Baca dan Edit RGB")
    print("-------------")
    print("1. Baca RGB")
    print("2. Edit RGB")
    print("3. Keluar")

    pilihan = input("Input pilihan: ")

    if pilihan == '1':
        Baca()
    elif pilihan == '2':
        Edit()
    elif pilihan == '3':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
    user_input = input("Press Enter to continue...")
    user_input = input()
    clear()
