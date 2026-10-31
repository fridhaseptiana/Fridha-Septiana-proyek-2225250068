
def tampilkan_data(data):
    print("\nDAFTAR NILAI MAHASISWA")
    print("-" * 65)
    print(f"{'NIM':<12}{'NAMA':<25}{'NILAI':>10}")
    print("-" * 65)

    for mahasiswa in data:
        print(
            f"{mahasiswa['nim']:<12}"
            f"{mahasiswa['nama']:<25}"
            f"{mahasiswa['nilai']:>10.2f}"
        )

    print("-" * 65)


def tampilkan_hasil_analisis(
    rata_rata,
    tertinggi,
    terendah,
    lulus,
    tidak_lulus
):
    print("\nHASIL ANALISIS NILAI MAHASISWA")
    print("-" * 40)
    print(f"Rata-rata nilai     : {rata_rata:.2f}")

    if tertinggi:
        print(
            f"Nilai tertinggi     : "
            f"{tertinggi['nama']} ({tertinggi['nilai']:.2f})"
        )

    if terendah:
        print(
            f"Nilai terendah      : "
            f"{terendah['nama']} ({terendah['nilai']:.2f})"
        )

    print(f"Jumlah mahasiswa lulus       : {lulus}")
    print(f"Jumlah mahasiswa tidak lulus : {tidak_lulus}")
    print("-" * 40)
