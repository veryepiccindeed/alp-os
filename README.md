# Basic CLI pada Sistem Linux Menggunakan Python

Proyek ini merupakan reimplementasi dari CLI dasar pada sistem Linux menggunakan bahasa pemrograman Python. CLI ini mendukung beberapa perintah dasar yang umum digunakan pada terminal Linux, serta beberapa perintah tambahan yang unik.

## Cara Menjalankan Program

1. Pastikan Anda memiliki Python 3 terinstal di sistem Anda.
2. Simpan file `basic_CLI.py` di komputer Anda.
3. Buka terminal atau command prompt.
4. Navigasikan ke direktori tempat Anda menyimpan file `basic_CLI.py`.
5. Jalankan program dengan perintah:

    ```bash
    python basic_CLI.py
    ```

## Daftar Perintah yang Diimplementasikan

### Perintah Wajib

| Perintah      | Deskripsi                                                                   | Contoh Penggunaan          |
| ------------- | --------------------------------------------------------------------------- | -------------------------- |
| `ls`          | Menampilkan daftar file dan folder di direktori saat ini.                   | `ls`                       |
| `pwd`         | Menampilkan direktori kerja saat ini.                                      | `pwd`                      |
| `cd <path>`   | Mengubah direktori kerja.                                                   | `cd Documents`             |
| `mkdir <dir>` | Membuat direktori baru.                                                    | `mkdir new_folder`         |
| `rmdir <dir>` | Menghapus direktori (jika kosong).                                         | `rmdir old_folder`         |
| `touch <file>`| Membuat file kosong baru.                                                  | `touch new_file.txt`       |
| `rm <file>`   | Menghapus file.                                                             | `rm old_file.txt`          |
| `cp <src> <dest>` | Menyalin file dari satu lokasi ke lokasi lain.                          | `cp file.txt backup.txt`   |
| `mv <src> <dest>` | Memindahkan atau mengganti nama file/direktori.                          | `mv file.txt new_location/` |
| `help`        | Menampilkan list perintah yang ada dan fungsinya.                           | `help`                     |
| `clear`       | Membersihkan layar terminal.                                                | `clear`                    |
| `exit`        | Keluar dari CLI.                                                            | `exit`                     |

### Perintah Tambahan

| Perintah       | Deskripsi                                                               | Contoh Penggunaan           |
| -------------- | ----------------------------------------------------------------------- | --------------------------- |
| `search <pattern>` | Mencari file atau direktori berdasarkan nama.                          | `search report.pdf`        |
| `tree`         | Menampilkan struktur direktori dalam bentuk pohon.                       | `tree`                      |
| `log <command>` | Menyimpan riwayat penggunaan command ke file log (`command_log.txt`). | `log ls -l`                 |
| `joke`         | Menampilkan lelucon acak.                                                | `joke`                      |

