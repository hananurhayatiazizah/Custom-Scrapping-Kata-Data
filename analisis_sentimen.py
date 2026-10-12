
import pandas as pd

# Membaca dataset yang sudah dibersihkan
df = pd.read_csv("komentar_bersih.csv")

# Kata-kata petunjuk untuk pemeriksaan awal.
# Label ini masih perlu diperiksa secara manual.
kata_negatif = [
    "susah", "buruk", "diganti", "peras", "gila",
    "aneh", "rakyat", "korupsi", "rampok", "malas",
    "hutang", "dipajakin", "dipajaki", "pajak lagi",
    "tidak adil", "tolol", "menderita", "bebani"
]

kata_positif = [
    "setuju", "bagus", "baik", "adil", "mendukung",
    "benar", "tidak kena", "belum kena"
]

def beri_label(teks):
    teks = str(teks).lower()

    skor_negatif = sum(kata in teks for kata in kata_negatif)
    skor_positif = sum(kata in teks for kata in kata_positif)

    if skor_negatif > skor_positif:
        return "Negatif"
    elif skor_positif > skor_negatif:
        return "Positif"
    else:
        return "Netral"

df["sentimen_awal"] = df["komentar"].apply(beri_label)

# Simpan hasil untuk diperiksa dan dikoreksi
df.to_csv(
    "hasil_sentimen_awal.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Analisis sentimen awal selesai.")
print("Jumlah data:", len(df))
print("\nDistribusi sentimen awal:")
print(df["sentimen_awal"].value_counts())
print("\nContoh hasil:")
print(df[["komentar", "sentimen_awal"]].head(10).to_string(index=False))
print("\nFile dibuat: hasil_sentimen_awal.csv")
