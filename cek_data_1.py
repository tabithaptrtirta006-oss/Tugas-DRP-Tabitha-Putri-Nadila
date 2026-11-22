import pandas as pd
# Membaca file CSV menjadi tabel (DataFrame)
df = pd.read_csv("indonesia_mbg_nationwide_enriched_2026.csv")

# Memeriksa ukuran dataset
print("Ukuran Dataset:")
print(df.shape)

# Memeriksa nama seluruh kolom
print("\nNama Kolom:")
for i, col in enumerate(df.columns, start=1):
    print(f"{i}.{col}")

# Memeriksa tipe data setiap kolom
print("\nTipe Data:")
print(df.dtypes)

# Memeriksa informasi lengkap dataset
print("\nInformasi Dataset:")
df.info()

# Menampilkan 5 data pertama
print("\n5 Data Pertama:")
print(df.head())

# Menampilkan 5 data terakhir
print("\n5 Data Terakhir:")
print(df.tail())

# Menampilkan 10 data secara acak
print("\n10 Data Acak:")
print(df.sample(10))

# Memeriksa jumlah data kosong setiap kolom
print("\nJumlah Missing Value:")
print(df.isnull().sum())

# Menghitung total seluruh missing value
print("\nTotal Missing Value:")
print(df.isnull().sum().sum())

# Menghitung jumlah data duplikat
print("\nJumlah Data Duplikat:")
print(df.duplicated().sum())

# Menampilkan data yang terduplikasi
print("\nData Duplikat:")
print(df[df.duplicated()])

# Statistik deskriptif seluruh variabel numerik
print("\nStatistik Deskriptif:")
print(df.describe())

# Statistik deskriptif yang termasuk variabel kategori
print("\nStatistik Seluruh Variabel:")
print(df.describe(include="all"))

# Memeriksa jumlah nilai unik setiap kolom
print("\nJumlah Nilai Unik:")
print(df.nunique())

# Memeriksa distribusi kategori provinsi
print("\nJumlah Data per Provinsi:")
print(df["province"].value_counts())

# Memeriksa kategori kepatuhan program
print("\nKategori Kepatuhan BGN:")
print(df["bgn_program_compliance_tier"].value_counts())

# Memeriksa jenis protein
print("\nJenis Protein:")
print(df["protein_type"].value_counts())

# Menghitung korelasi antarvariabel numerik
print("\nKorelasi Antarvariabel:")
print(df.corr(numeric_only=True))

# Menghitung rata-rata biaya makanan setiap provinsi
print("\nRata-rata Biaya MBG per Provinsi:")
print(df.groupby("province")["total_meal_cost_idr"].mean())

# Menghitung rata-rata sisa makanan setiap provinsi
print("\nRata-rata Sisa Makanan per Provinsi:")
print(df.groupby("province")["plate_waste_percentage"].mean())

# Menghitung jumlah distribusi setiap provinsi
print("\nJumlah Distribusi per Provinsi:")
print(df.groupby("province")["distribution_id"].count())