import os
import pandas as pd
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

# Ventas por ciudad
q1 = """
SELECT city, SUM(ventas_totales) AS ventas
FROM data_mart_ventas
GROUP BY city
ORDER BY ventas DESC;
"""
print("=== Ventas por ciudad ===")
print(pd.read_sql(q1, engine))

# Ventas por categoría
q2 = """
SELECT category, SUM(ventas_totales) AS ventas
FROM data_mart_ventas
GROUP BY category
ORDER BY ventas DESC;
"""
print("\n=== Ventas por categoría ===")
print(pd.read_sql(q2, engine))

# Método de pago más usado
q3 = """
SELECT payment_method, SUM(unidades_vendidas) AS unidades
FROM data_mart_ventas
GROUP BY payment_method
ORDER BY unidades DESC;
"""
print("\n=== Método de pago más usado ===")
print(pd.read_sql(q3, engine))