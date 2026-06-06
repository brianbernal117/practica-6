import pandas as pd

# 1. Cargar dataset
df = pd.read_csv("walmart_sales.csv")

# 2. Vista inicial
print(df.head())
print(df.info())
print(df.isnull().sum())
print("Duplicados:", df.duplicated().sum())

# 3. Limpiar duplicados y nulos
df = df.drop_duplicates()
df = df.dropna()

# 4. Normalizar nombres de columnas para PostgreSQL
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
    .str.replace("%", "pct", regex=False)
)

# 5. Convertir fecha
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day

# 6. Guardar versión limpia
df.to_csv("walmart_sales_clean.csv", index=False)
print("Dataset limpio guardado como walmart_sales_clean.csv")