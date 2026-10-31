# TEST CASE - PENGUJIAN PROGRAM

## Program Pengolahan dan Analisis Data Nilai Mahasiswa

### 1. Tujuan Pengujian
Pengujian dilakukan untuk memastikan program dapat membaca data, memvalidasi data, melakukan perhitungan, dan menampilkan hasil analisis nilai mahasiswa dengan benar.

### 2. Data Pengujian
Data pengujian menggunakan file `data/contoh_data.txt` yang berisi 10 mahasiswa.

### 3. Daftar Test Case

| No. | Pengujian | Data/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| 1 | Membaca data | File tersedia dan berisi data valid | Data mahasiswa berhasil dibaca |
| 2 | Menghitung rata-rata | 10 data nilai mahasiswa | Rata-rata 76.30 |
| 3 | Nilai tertinggi | Seluruh data mahasiswa | Fajar Ramadhan, nilai 95 |
| 4 | Nilai terendah | Seluruh data mahasiswa | Gita Permata, nilai 55 |
| 5 | Menghitung kelulusan | Batas kelulusan 60 | 9 mahasiswa lulus dan 1 tidak lulus |
| 6 | Nilai berbentuk huruf | Nilai berupa teks, misalnya abc | Data tidak valid dilewati |
| 7 | Nilai di luar rentang | Nilai kurang dari 0 atau lebih dari 100 | Data tidak valid dilewati |
| 8 | Data tidak lengkap | Jumlah kolom tidak sesuai | Data tidak valid dilewati |
| 9 | File tidak ditemukan | File tidak tersedia | Program menampilkan pesan kesalahan |

### 4. Hasil Pengujian

Berdasarkan pengujian yang telah dilakukan, program berhasil membaca dan mengolah 10 data mahasiswa dengan hasil sebagai berikut:

- Jumlah data mahasiswa: 10 orang.
- Rata-rata nilai: 76.30.
- Nilai tertinggi: Fajar Ramadhan (95).
- Nilai terendah: Gita Permata (55).
- Jumlah mahasiswa lulus: 9 orang.
- Jumlah mahasiswa tidak lulus: 1 orang.

Hasil pengujian menunjukkan bahwa perhitungan rata-rata, pencarian nilai tertinggi dan terendah, serta penghitungan kelulusan telah menghasilkan nilai yang sesuai dengan hasil yang diharapkan.

Screenshot hasil program disimpan pada folder `docs/screenshot/hasil_analisis.png` sebagai bukti dokumentasi pengujian.

### 5. Kesimpulan
Test case digunakan untuk memeriksa setiap fungsi program, mulai dari pembacaan data hingga analisis nilai mahasiswa. Pengujian membantu memastikan program berjalan dengan benar dan dapat menangani data yang tidak valid.
