from PIL import Image

def to_binary(data):
    # Konversi data menjadi format biner string
    if isinstance(data, str):
        return ''.join(format(ord(c), '08b') for c in data)
    elif isinstance(data, bytes):
        return ''.join(format(byte, '08b') for byte in data)
    else:
        raise TypeError("Tipe data tidak didukung.")

def encode_text_to_image(image_path, text, output_path):
    original_image = Image.open(image_path)
    encoded_image = original_image.copy()
    binary_text = to_binary(text) + '1111111111111110'  # Menambahkan delimiter

    if len(binary_text) > (original_image.width * original_image.height * 3):
        raise ValueError("Gambar terlalu kecil atau pesan terlalu besar.")

    index = 0
    for x in range(original_image.width):
        for y in range(original_image.height):
            pixel = list(original_image.getpixel((x, y)))
            for color_channel in range(3):
                if index < len(binary_text):
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_text[index], 2)
                    index += 1
            encoded_image.putpixel((x, y), tuple(pixel))

    encoded_image.save(output_path)

def decode_text_from_image(image_path):
    encoded_image = Image.open(image_path)
    binary_text = ''

    for x in range(encoded_image.width):
        for y in range(encoded_image.height):
            pixel = list(encoded_image.getpixel((x, y)))
            for color_channel in range(3):
                binary_text += format(pixel[color_channel], '08b')[-1]

    delimiter_index = binary_text.find('1111111111111110')
    if delimiter_index != -1:
        binary_text = binary_text[:delimiter_index]

    try:
        text = ''.join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8))
        return text
    except ValueError:
        return "Pesan tidak ditemukan atau tidak valid."

def main():
    while True:
        print("1. Encode teks ke dalam gambar")
        print("2. Decode teks dari gambar")
        print("3. Keluar")
        choice = input("Pilih opsi (1/2/3): ")

        if choice == "1":
            image_path = input("Masukkan path gambar input: ")
            text = input("Masukkan teks yang ingin disisipkan: ")
            output_path = input("Masukkan path gambar output: ")
            encode_text_to_image(image_path, text, output_path)
            print("Teks berhasil disisipkan ke dalam gambar.")
        elif choice == "2":
            image_path = input("Masukkan path gambar yang ingin didecode: ")
            decoded_text = decode_text_from_image(image_path)
            print("Teks yang didekodekan:", decoded_text)
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()
