
# Custom Web Scraping Berita E-Commerce Katadata

## Deskripsi Proyek
Proyek ini dibuat untuk tugas mata kuliah SOSMED.
Program menggunakan Python untuk mengambil data artikel berita
dari kategori E-Commerce di website Katadata.co.id.

## Tujuan
Mengumpulkan informasi berita yang berkaitan dengan bisnis digital,
khususnya isu marketplace dan kebijakan pajak seller, untuk
membantu mengidentifikasi topik yang dibahas dalam berita e-commerce.

## Sumber Data
- Kategori: https://katadata.co.id/digital/e-commerce
- Artikel utama:
  https://katadata.co.id/digital/e-commerce/6abf1f2321669/pajak-seller-dipungut-per-1-oktober-asosiasi-marketplace-ungkap-potensi-kendala

## Teknologi
- Python
- Requests
- BeautifulSoup4
- Pandas

## Data yang Dikumpulkan
- Judul artikel
- Nama penulis
- Tanggal publikasi
- Deskripsi artikel
- Isi artikel jika tersedia
- URL sumber
- Waktu scraping

## Cara Menjalankan
1. Instal Python.
2. Instal library:
   `python -m pip install requests beautifulsoup4 pandas`
3. Jalankan:
   `python scrapper.py`
4. Hasil akan disimpan dalam `hasil_scraping.csv`.

## Output
File CSV berisi data artikel yang berhasil diambil
dari halaman sumber.

## Catatan
Jumlah dan kelengkapan data bergantung pada halaman yang
tersedia serta struktur HTML saat scraping dilakukan.
Pengambilan data dilakukan dengan memperhatikan ketentuan
akses website.
