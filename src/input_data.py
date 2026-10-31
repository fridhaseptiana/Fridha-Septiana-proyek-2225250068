
def baca_data(nama_file):
    data_mahasiswa = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            next(file, None)

            for nomor_baris, baris in enumerate(file, start=2):
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",")

                if len(bagian) != 3:
                    print(f"Baris {nomor_baris} tidak valid.")
                    continue

                nim, nama, nilai = bagian

                try:
                    nilai = float(nilai)
                except ValueError:
                    print(f"Nilai pada baris {nomor_baris} bukan angka.")
                    continue

                if not nim.strip() or not nama.strip():
                    print(f"Data pada baris {nomor_baris} tidak lengkap.")
                    continue

                if nilai < 0 or nilai > 100:
                    print(f"Nilai pada baris {nomor_baris} di luar rentang 0-100.")
                    continue

                mahasiswa = {
                    "nim": nim.strip(),
                    "nama": nama.strip(),
                    "nilai": nilai
                }

                data_mahasiswa.append(mahasiswa)

    except FileNotFoundError:
        print("File data mahasiswa tidak ditemukan.")

    except OSError:
        print("Terjadi kesalahan saat membaca file.")

    return data_mahasiswa
