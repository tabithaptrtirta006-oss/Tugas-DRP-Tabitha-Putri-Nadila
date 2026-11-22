import pandas as pd
# Membaca file CSV menjadi tabel (DataFrame)
df = pd.read_csv("indonesia_mbg_nationwide_enriched_2026.csv")

# Memeriksa nilai tidak wajar
print("\n=== Pemeriksaan Nilai Tidak Wajar ===")

# Jarak distribusi negatif
print("Jarak Negatif:")
print((df["delivery_distance_km"] < 0).sum())

# Waktu transit negatif
print("Waktu Transit Negatif:")
print((df["transit_time_minutes"] < 0).sum())

# Kapasitas dapur nol atau negatif
print("Kapasitas Dapur Tidak Valid:")
print((df["kitchen_daily_capacity_portions"] <= 0).sum())

# Biaya makanan negatif
print("Biaya Makanan Negatif:")
print((df["total_meal_cost_idr"] < 0).sum())

# Kalori negatif atau nol
print("Kalori Tidak Valid:")
print((df["estimated_calories_kcal"] <= 0).sum())

# Protein negatif atau nol
print("Protein Tidak Valid:")
print((df["estimated_protein_grams"] <= 0).sum())

# Memeriksa batas nilai variabel
print("\n=== Pemeriksaan Batas Nilai ===")

# Persentase harus berada pada 0-100
print("Plate Waste Tidak Valid:")
print((~df["plate_waste_percentage"].between(0, 100)).sum())

print("Attendance Tidak Valid:")
print((~df["student_attendance_rate_pct"].between(0, 100)).sum())

print("Local Sourcing Tidak Valid:")
print((~df["local_farmer_sourcing_pct"].between(0, 100)).sum())

# Indeks dan skor harus berada pada 0-10
print("Spoilage Risk Tidak Valid:")
print((~df["spoilage_risk_index"].between(0, 10)).sum())

print("Economic Score Tidak Valid:")
print((~df["local_economic_multiplier_score"].between(0, 10)).sum())

# Confidence score harus berada pada 0-1
print("Confidence Score Tidak Valid:")
print((~df["confidence_score"].between(0, 1)).sum())

# Mendeteksi outlier menggunakan IQR
print("\n=== Deteksi Outlier Metode IQR ===")

# Mengambil seluruh kolom numerik
kolom_numerik = df.select_dtypes(include="number").columns

for kolom in kolom_numerik:

    Q1 = df[kolom].quantile(0.25)
    Q3 = df[kolom].quantile(0.75)

    IQR = Q3 - Q1

    batas_bawah = Q1 - 1.5 * IQR
    batas_atas = Q3 + 1.5 * IQR

    outlier = df[
        (df[kolom] < batas_bawah) |
        (df[kolom] > batas_atas)
    ]

    print("\nVariabel:", kolom)
    print("Batas Bawah:", batas_bawah)
    print("Batas Atas:", batas_atas)
    print("Jumlah Outlier:", len(outlier))

# Memeriksa konsistensi data kategori
print("\n=== Pemeriksaan Data Kategori ===")

kolom_kategori = df.select_dtypes(
    include=["object", "str"]
).columns

for kolom in kolom_kategori:

    # Mengabaikan kolom identitas
    if kolom == "distribution_id":
        continue

    print("\nVariabel:", kolom)

    print("Jumlah kategori:")
    print(df[kolom].nunique())

    print("Jumlah spasi di awal/akhir:")
    print(
        df[kolom].str.strip().ne(df[kolom]).sum()
    )