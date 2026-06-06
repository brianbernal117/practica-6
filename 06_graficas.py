import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

load_dotenv()

engine = create_engine(URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
), connect_args={"sslmode": "require"})

df = pd.read_sql("SELECT * FROM data_mart_ventas", engine)

# Gráfica 1 - Ventas por categoría
ventas_categoria = df.groupby("category")["ventas_totales"].sum().sort_values()
ventas_categoria.plot(kind="barh", color="steelblue")
plt.title("Ventas totales por categoría")
plt.xlabel("Ventas")
plt.ylabel("Categoría")
plt.tight_layout()
plt.savefig("grafica_categorias.png")
plt.close()
print("Gráfica 1 guardada: grafica_categorias.png")

# Gráfica 2 - Ventas por ciudad
ventas_ciudad = df.groupby("city")["ventas_totales"].sum().sort_values(ascending=False)
ventas_ciudad.plot(kind="bar", color="coral")
plt.title("Ventas totales por ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Ventas")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("grafica_ciudades.png")
plt.close()
print("Gráfica 2 guardada: grafica_ciudades.png")

# Gráfica 3 - Método de pago
ventas_pago = df.groupby("payment_method")["unidades_vendidas"].sum()
ventas_pago.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Unidades vendidas por método de pago")
plt.ylabel("")
plt.tight_layout()
plt.savefig("grafica_pagos.png")
plt.close()
print("Gráfica 3 guardada: grafica_pagos.png")