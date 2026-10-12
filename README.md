# Custom Scraping Komentar X dan Analisis Sentimen

## Deskripsi Proyek

Proyek ini dibuat untuk mengumpulkan komentar pengguna dari media sosial X (Twitter) menggunakan Python dan API TwitterAPIs. Data yang diperoleh kemudian dibersihkan dan dipersiapkan untuk analisis sentimen.

Topik yang digunakan adalah tanggapan pengguna terhadap kebijakan Pajak Penghasilan (PPh) Pasal 22 bagi pedagang marketplace, berdasarkan balasan pada unggahan detikcom di X.

## Tujuan

1. Mengumpulkan komentar pengguna X melalui API.
2. Menyimpan data komentar dalam format CSV.
3. Membersihkan data dari username yang disebut, tautan, dan teks yang tidak diperlukan untuk analisis.
4. Melakukan pelabelan sentimen awal menjadi positif, negatif, dan netral.
5. Menyiapkan dataset untuk pemeriksaan dan analisis lebih lanjut.

## Sumber Data

- Platform: X (Twitter)
- Akun sumber: detikcom
- Tautan unggahan: https://x.com/detikcom/status/1944759450113659310
- Topik: Tanggapan pengguna terhadap kebijakan pajak bagi pedagang marketplace.

## Teknologi yang Digunakan

- Python
- Pandas
- Requests
- TwitterAPIs
- Git dan GitHub

## Struktur File

| File | Keterangan |
|---|---|
| `replies.py` | Program untuk mengambil balasan dari unggahan X. |
| `komentar_x.csv` | Dataset mentah hasil scraping. |
| `komentar_bersih.csv` | Dataset setelah proses pembersihan teks. |
| `analisis_sentimen.py` | Program pelabelan sentimen awal berbasis kata kunci. |
| `hasil_sentimen_awal.csv` | Hasil pelabelan sentimen otomatis awal. |
| `hasil_sentimen_review.csv` | Dataset untuk pemeriksaan dan koreksi label secara manual. |
| `scrapper.py` | Program scraping Katadata dari tahap proyek sebelumnya. |
| `hasil_scraping.csv` | Hasil scraping Katadata dari tahap proyek sebelumnya. |
| `requirements.txt` | Daftar pustaka Python yang diperlukan. |

## Hasil Sementara

Scraping awal berhasil menghasilkan 51 komentar unik dari tiga halaman hasil API. Setelah pembersihan, tersisa 46 komentar untuk pemeriksaan lebih lanjut.

Pelabelan sentimen awal dilakukan dengan pencocokan kata sederhana. Hasilnya belum merupakan klasifikasi final dan masih perlu diperiksa, khususnya pada komentar sarkastis, komentar yang berisi pertanyaan, serta komentar yang tidak relevan.

## Cara Menjalankan

### 1. Instal dependensi

```bash
pip install -r requirements.txt
```

### 2. Atur API key

Simpan API key TwitterAPIs melalui environment variable `TWITTERAPIS_KEY`. Jangan menuliskan API key secara langsung di dalam kode atau mengunggahnya ke GitHub.

Pada PowerShell:

```powershell
$env:TWITTERAPIS_KEY = Read-Host "Masukkan API key TwitterAPIs"
```

### 3. Jalankan scraping

```bash
python replies.py
```

### 4. Jalankan analisis sentimen awal

```bash
python analisis_sentimen.py
```

## Keterbatasan

Dataset yang digunakan masih terbatas pada komentar yang berhasil dikumpulkan dari satu unggahan. Pelabelan sentimen menggunakan pencocokan kata sederhana sehingga dapat menghasilkan kesalahan, terutama pada sarkasme dan konteks bahasa informal. Hasil perlu diperiksa sebelum digunakan untuk menarik kesimpulan.

## Keamanan

API key merupakan informasi rahasia. Gunakan environment variable dan jangan mengunggah kredensial ke repository publik.

## Status Proyek

Proyek ini merupakan tugas pembelajaran *custom scraping* dan analisis sentimen menggunakan Python.