import os  # Library untuk berinteraksi dengan sistem operasi, seperti manipulasi file dan direktori
import sys  # Library untuk mengakses variabel dan fungsi yang berinteraksi dengan interpreter Python
import shutil  # Library untuk operasi file tingkat tinggi, seperti menyalin dan memindahkan file
import datetime  # Library untuk memanipulasi tanggal dan waktu
import random  # Library untuk menghasilkan angka acak

def ls():
    """Menampilkan daftar file dan folder di direktori saat ini."""
    items = os.listdir()  # Mengambil daftar semua file dan direktori di direktori saat ini
    print(" ".join(items))  # Menampilkan item dengan spasi sebagai pemisah

def pwd():
    """Menampilkan direktori kerja saat ini."""
    print(os.getcwd())  # Mengambil dan mencetak direktori kerja saat ini

def cd(path):
    """Mengubah direktori kerja."""
    try:
        os.chdir(path)  # Mencoba mengubah direktori kerja ke path yang diberikan
    except FileNotFoundError:
        print(f"cd: {path}: No such file or directory")  # Menampilkan pesan error jika direktori tidak ditemukan
    except NotADirectoryError:
        print(f"cd: {path}: Not a directory")  # Menampilkan pesan error jika path bukan direktori

def mkdir(dirname):
    """Membuat direktori baru."""
    try:
        os.mkdir(dirname)  # Mencoba membuat direktori baru dengan nama yang diberikan
    except FileExistsError:
        print(f"mkdir: cannot create directory '{dirname}': File exists")  # Menampilkan pesan error jika direktori sudah ada
    except OSError as e:
        print(f"mkdir: cannot create directory '{dirname}': {e.strerror}")  # Menampilkan pesan error jika terjadi kesalahan lain

def rmdir(dirname):
    """Menghapus direktori (jika kosong)."""
    try:
        os.rmdir(dirname)  # Mencoba menghapus direktori dengan nama yang diberikan
    except FileNotFoundError:
        print(f"rmdir: failed to remove '{dirname}': No such file or directory")  # Menampilkan pesan error jika direktori tidak ditemukan
    except OSError as e:
        print(f"rmdir: failed to remove '{dirname}': {e.strerror}")  # Menampilkan pesan error jika direktori tidak kosong atau kesalahan lain

def touch(filename):
    """Membuat file kosong baru."""
    try:
        open(filename, 'a').close()  # Mencoba membuat file kosong dengan nama yang diberikan (mode 'a' untuk append, tapi langsung ditutup)
    except OSError as e:
        print(f"touch: cannot create file '{filename}': {e.strerror}")  # Menampilkan pesan error jika terjadi kesalahan

def rm(filename):
    """Menghapus file."""
    try:
        os.remove(filename)  # Mencoba menghapus file dengan nama yang diberikan
    except FileNotFoundError:
        print(f"rm: cannot remove '{filename}': No such file or directory")  # Menampilkan pesan error jika file tidak ditemukan
    except IsADirectoryError:
        print(f"rm: cannot remove '{filename}': Is a directory")  # Menampilkan pesan error jika yang diberikan adalah direktori

def cp(src, dest):
    """Menyalin file dari satu lokasi ke lokasi lain."""
    try:
        shutil.copy2(src, dest)  # Mencoba menyalin file dari src ke dest, mempertahankan metadata
    except FileNotFoundError:
        print(f"cp: cannot copy '{src}': No such file or directory")  # Menampilkan pesan error jika file sumber tidak ditemukan
    except shutil.SameFileError:
        print(f"cp: '{src}' and '{dest}' are the same file")  # Menampilkan pesan error jika src dan dest adalah file yang sama
    except IsADirectoryError:
        print(f"cp: '{dest}' is a directory, not a file")  # Menampilkan pesan error jika dest adalah direktori
    except PermissionError:
        print(f"cp: permission denied to copy '{src}' to '{dest}'")  # Menampilkan pesan error jika tidak ada izin untuk menyalin

def mv(src, dest):
    """Memindahkan atau mengganti nama file/direktori."""
    try:
        shutil.move(src, dest)  # Mencoba memindahkan file/direktori dari src ke dest
    except FileNotFoundError:
        print(f"mv: cannot move '{src}': No such file or directory")  # Menampilkan pesan error jika file/direktori sumber tidak ditemukan
    except shutil.Error as e:
        print(f"mv: {e}")  # Menampilkan pesan error jika terjadi kesalahan lain

def help():
    """Menampilkan list perintah yang ada dan fungsinya."""
    print("ls - Menampilkan daftar file dan folder")
    print("pwd - Menampilkan direktori kerja saat ini")
    print("cd <path> - Mengubah direktori kerja")
    print("mkdir <dirname> - Membuat direktori baru")
    print("rmdir <dirname> - Menghapus direktori (jika kosong)")
    print("touch <filename> - Membuat file kosong baru")
    print("rm <filename> - Menghapus file")
    print("cp <src> <dest> - Menyalin file dari satu lokasi ke lokasi lain")
    print("mv <src> <dest> - Memindahkan atau mengganti nama file/direktori")
    print("help - Menampilkan list perintah yang ada dan fungsinya")
    print("clear - Membersihkan layar terminal")
    print("exit - Keluar dari CLI")
    print("search <pattern> - Mencari file atau direktori berdasarkan nama")
    print("tree - Menampilkan struktur direktori dalam bentuk pohon")
    print("log <command> - Menyimpan riwayat penggunaan command ke file log")
    print("joke - Menampilkan lelucon acak")

def clear():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Menjalankan perintah 'cls' di Windows dan 'clear' di sistem Unix-like

def search(pattern):
    """Mencari file atau direktori berdasarkan nama."""
    for root, dirs, files in os.walk("."):  # Menelusuri semua file dan direktori mulai dari direktori saat ini (".")
        for item in dirs + files:  # Iterasi melalui semua direktori dan file
            if pattern in item:  # Memeriksa apakah pola ada dalam nama item
                print(os.path.join(root, item))  # Mencetak path lengkap item yang cocok

def tree(path=".", level=0):
    """Menampilkan struktur direktori dalam bentuk pohon."""
    if level == 0:
        print(".")  # Cetak direktori saat ini sebagai root dari pohon
    
    try:
        items = os.listdir(path)  # Ambil daftar item di path yang diberikan
    except PermissionError:
        print(" " * 4 * (level + 1) + "├── [Permission Denied]")  # Cetak pesan jika tidak ada izin akses
        return
    
    items.sort()  # Urutkan item untuk konsistensi tampilan
    
    for i, item in enumerate(items):
        item_path = os.path.join(path, item)  # Buat path lengkap untuk item saat ini
        is_last_item = (i == len(items) - 1)  # Cek apakah item ini adalah item terakhir dalam daftar
        
        try:
            if os.path.isdir(item_path):  # Jika item adalah direktori
                print(" " * 4 * level + ("└── " if is_last_item else "├── ") + item)  # Cetak nama direktori dengan indentasi yang sesuai
                tree(item_path, level + 1)  # Panggil fungsi tree secara rekursif untuk subdirektori
            else:  # Jika item adalah file
                print(" " * 4 * level + ("└── " if is_last_item else "├── ") + item)  # Cetak nama file dengan indentasi yang sesuai
        except PermissionError:
            print(" " * 4 * (level + 1) + "├── [Permission Denied]")  # Cetak pesan jika tidak ada izin akses

def log_command(command):
    """Menyimpan riwayat penggunaan command ke file log."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Dapatkan waktu saat ini dalam format yang ditentukan
    with open("command_log.txt", "a") as log_file:  # Buka file log dalam mode append
        log_file.write(f"{timestamp} - {command}\n")  # Tulis timestamp dan perintah ke file log

def joke():
    """Menampilkan lelucon acak."""
    jokes = [  # Daftar lelucon
        "Why did the programmer quit his job? Because he didn't get arrays!",
        "Why do Java developers wear glasses? Because they don't see sharp!",
        "How do you comfort a JavaScript bug? You console it!",
        "Why was the computer cold? It left its Windows open!",
        "What's a computer's favorite snack? Microchips!"
    ]
    print(random.choice(jokes))  # Cetak lelucon yang dipilih secara acak

def main():
    """Fungsi utama untuk menjalankan CLI."""
    print("Selamat datang di CLI sederhana!")
    print("Ketik 'help' untuk melihat daftar perintah yang tersedia.")

    while True:  # Loop utama CLI
        try:
            user_input = input(f"{os.getcwd()} $ ")  # Menampilkan prompt dan mengambil input dari pengguna
            log_command(user_input)  # Catat perintah ke dalam file log
            command_parts = user_input.split()  # Memisahkan input menjadi bagian-bagian berdasarkan spasi
            command = command_parts[0]  # Mengambil bagian pertama sebagai perintah

            # Percabangan untuk setiap perintah
            if command == "ls":
                ls()  # Panggil fungsi ls()
            elif command == "pwd":
                pwd()  # Panggil fungsi pwd()
            elif command == "cd":
                if len(command_parts) > 1:
                    cd(command_parts[1])  # Panggil fungsi cd() dengan argumen path
                else:
                    cd(os.path.expanduser("~"))  # Panggil fungsi cd() untuk ke home directory jika tidak ada argumen
            elif command == "mkdir":
                if len(command_parts) > 1:
                    mkdir(command_parts[1])  # Panggil fungsi mkdir() dengan argumen nama direktori
                else:
                    print("mkdir: missing operand")  # Cetak pesan error jika tidak ada argumen
            elif command == "rmdir":
                if len(command_parts) > 1:
                    rmdir(command_parts[1])  # Panggil fungsi rmdir() dengan argumen nama direktori
                else:
                    print("rmdir: missing operand")  # Cetak pesan error jika tidak ada argumen
            elif command == "touch":
                if len(command_parts) > 1:
                    touch(command_parts[1])  # Panggil fungsi touch() dengan argumen nama file
                else:
                    print("touch: missing file operand")  # Cetak pesan error jika tidak ada argumen
            elif command == "rm":
                if len(command_parts) > 1:
                    rm(command_parts[1])  # Panggil fungsi rm() dengan argumen nama file
                else:
                    print("rm: missing operand")  # Cetak pesan error jika tidak ada argumen
            elif command == "cp":
                if len(command_parts) > 2:
                    cp(command_parts[1], command_parts[2])  # Panggil fungsi cp() dengan argumen file sumber dan tujuan
                else:
                    print("cp: missing file operand")  # Cetak pesan error jika argumen kurang
            elif command == "mv":
                if len(command_parts) > 2:
                    mv(command_parts[1], command_parts[2])  # Panggil fungsi mv() dengan argumen file sumber dan tujuan
                else:
                    print("mv: missing file operand")  # Cetak pesan error jika argumen kurang
            elif command == "help":
                help()  # Panggil fungsi help()
            elif command == "clear":
                clear()  # Panggil fungsi clear()
            elif command == "search":
                if len(command_parts) > 1:
                    search(command_parts[1])  # Panggil fungsi search() dengan argumen pola
                else:
                    print("search: missing operand")  # Cetak pesan error jika tidak ada argumen
            elif command == "tree":
                if len(command_parts) > 1:
                    tree(command_parts[1])  # Panggil fungsi tree() dengan argumen path
                else:
                    tree()  # Panggil fungsi tree() tanpa argumen untuk direktori saat ini
            elif command == "log":
                if len(command_parts) > 1:
                    log_command(" ".join(command_parts[1:]))  # Panggil fungsi log_command() dengan argumen perintah yang dijalankan
                    print(f"Command '{' '.join(command_parts[1:])}' logged.")
                else:
                    print("log: missing command to log")  # Cetak pesan error jika tidak ada argumen
            elif command == "joke":
                joke()  # Panggil fungsi joke()
            elif command == "exit":
                print("Keluar dari CLI.")
                sys.exit()  # Keluar dari program
            else:
                print(f"Perintah tidak dikenali: {command}")  # Cetak pesan error jika perintah tidak dikenali
        except KeyboardInterrupt:
            print("\nKeluar dari CLI.")  # Tangani interupsi Ctrl+C
            sys.exit()
        except EOFError:
            print("\nKeluar dari CLI.")  # Tangani interupsi Ctrl+D
            sys.exit()
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")  # Tangani exception yang tidak terduga

if __name__ == "__main__":
    main()  # Jalankan fungsi main() jika skrip ini dijalankan sebagai program utama