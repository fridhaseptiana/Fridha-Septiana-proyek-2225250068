
def hitung_rata_rata(data):
    if not data:
        return 0

    total_nilai = sum(mahasiswa["nilai"] for mahasiswa in data)
    return total_nilai / len(data)


def cari_nilai_tertinggi(data):
    if not data:
        return None

    return max(data, key=lambda mahasiswa: mahasiswa["nilai"])


def cari_nilai_terendah(data):
    if not data:
        return None

    return min(data, key=lambda mahasiswa: mahasiswa["nilai"])


def hitung_kelulusan(data):
    lulus = 0
    tidak_lulus = 0

    for mahasiswa in data:
        if mahasiswa["nilai"] >= 60:
            lulus += 1
        else:
            tidak_lulus += 1

    return lulus, tidak_lulus
