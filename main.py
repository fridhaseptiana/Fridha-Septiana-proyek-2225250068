
from pathlib import Path

from src.input_data import baca_data
from src.proses import (
    hitung_rata_rata,
    cari_nilai_tertinggi,
    cari_nilai_terendah,
    hitung_kelulusan
)
from src.output import (
    tampilkan_data,
    tampilkan_hasil_analisis
)


def main():
    lokasi_file = Path(__file__).parent / "data" / "contoh_data.txt"

    print("=" * 50)
    print("PROGRAM PENGOLAHAN DAN ANALISIS DATA NILAI MAHASISWA")
    print("=" * 50)

    data = baca_data(lokasi_file)

    if not data:
        print("Tidak ada data mahasiswa yang dapat diproses.")
        return

    rata_rata = hitung_rata_rata(data)
    tertinggi = cari_nilai_tertinggi(data)
    terendah = cari_nilai_terendah(data)
    lulus, tidak_lulus = hitung_kelulusan(data)

    tampilkan_data(data)

    tampilkan_hasil_analisis(
        rata_rata,
        tertinggi,
        terendah,
        lulus,
        tidak_lulus
    )


if __name__ == "__main__":
    main()
