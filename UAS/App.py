from PIL import Image
from tkinter import Tk, Label, Button, Entry, filedialog, Menu, LabelFrame

def text_to_binary(text):
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary

def hide_message(image_path, secret_message, output_path):
    img = Image.open(image_path)
    width, height = img.size
    secret_message += "#####"  # Tandai akhir pesan
    binary_message = text_to_binary(secret_message)
    message_length = len(binary_message)

    if message_length > (width * height):
        return "Pesan terlalu besar untuk disisipkan dalam gambar ini"

    index = 0
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))

            if index < message_length:
                r &= 0xFE  # Set LSB r ke 0
                r |= int(binary_message[index])
                index += 1

            img.putpixel((x, y), (r, g, b))

    img.save(output_path)
    return "Pesan berhasil disisipkan dalam gambar"

def reveal_message(image_path):
    img = Image.open(image_path)
    binary_message = ''

    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, _, _ = img.getpixel((x, y))
            binary_message += str(r & 1)

    split_message = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ''.join(chr(int(char, 2)) for char in split_message)

    end_marker_index = message.find("#####")
    if end_marker_index != -1:
        return message[:end_marker_index]
    else:
        return "Tidak ada pesan tersembunyi dalam gambar ini"

def select_image_hide():
    global image_path_hide
    image_path_hide = filedialog.askopenfilename(title="Pilih File Gambar", filetypes=(("Image files", "*.jpg;*.png;*.jpeg"), ("All files", "*.*")))
    if image_path_hide:
        label_image_hide.config(text=f"File Gambar Terpilih: {image_path_hide}")

def select_image_reveal():
    global image_path_reveal
    image_path_reveal = filedialog.askopenfilename(title="Pilih File Gambar", filetypes=(("Image files", "*.jpg;*.png;*.jpeg"), ("All files", "*.*")))
    if image_path_reveal:
        label_image_reveal.config(text=f"File Gambar Terpilih: {image_path_reveal}")

def process_hide():
    global image_path_hide
    output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
    if output_path:
        pesan_rahasia = entry_pesan.get()
        result = hide_message(image_path_hide, pesan_rahasia, output_path)
        label_status_hide.config(text=result)

def process_reveal():
    global image_path_reveal
    result = reveal_message(image_path_reveal)
    if result != "Tidak ada pesan tersembunyi dalam gambar ini":
        label_status_reveal.config(text="Pesan tersembunyi: " + result)
    else:
        label_status_reveal.config(text=result)

def show_hide_menu():
    frame_hide.pack()
    frame_reveal.pack_forget()

def show_reveal_menu():
    frame_hide.pack_forget()
    frame_reveal.pack()

# GUI setup
root = Tk()
root.title("Aplikasi Steganografi Gambar")

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Sembunyikan Pesan", command=show_hide_menu)
file_menu.add_command(label="Tampilkan Pesan", command=show_reveal_menu)
file_menu.add_separator()
file_menu.add_command(label="Keluar", command=root.quit)

frame_hide = LabelFrame(root, text="Sembunyikan pesan dalam gambar", padx=20, pady=20)
frame_reveal = LabelFrame(root, text="Temukan pesan tersembunyi dalam gambar", padx=20, pady=20)

# Komponen untuk menyembunyikan pesan
label_hide_instructions = Label(frame_hide, text="Sembunyikan pesan dalam gambar")
label_hide_instructions.pack()

button_choose_image_hide = Button(frame_hide, text="Pilih Gambar", command=select_image_hide)
button_choose_image_hide.pack()

label_image_hide = Label(frame_hide, text="Belum ada file gambar terpilih")
label_image_hide.pack()

label_pesan_hide = Label(frame_hide, text="Masukkan pesan:")
label_pesan_hide.pack()

entry_pesan = Entry(frame_hide)
entry_pesan.pack()

button_process_hide = Button(frame_hide, text="Sembunyikan Pesan", command=process_hide)
button_process_hide.pack()

label_status_hide = Label(frame_hide, text="")
label_status_hide.pack()

# Komponen untuk mengungkap pesan
label_reveal_instructions = Label(frame_reveal, text="Temukan pesan tersembunyi dalam gambar")
label_reveal_instructions.pack()

button_choose_image_reveal = Button(frame_reveal, text="Pilih Gambar", command=select_image_reveal)
button_choose_image_reveal.pack()

label_image_reveal = Label(frame_reveal, text="Belum ada file gambar terpilih")
label_image_reveal.pack()

button_process_reveal = Button(frame_reveal, text="Temukan Pesan", command=process_reveal)
button_process_reveal.pack()

label_status_reveal = Label(frame_reveal, text="")
label_status_reveal.pack()

root.mainloop()