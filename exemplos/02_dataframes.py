"""
DataFrames - Operações Básicas
===============================
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min

spark = SparkSession.builder \
    .appName("DataFrames") \
    .master("local[*]") \
    .getOrCreate()

# Dados de exemplo
dados = [
    (1, "João", "TI", 5000, 25),
    (2, "Maria", "RH", 6000, 30),
    (3, "Pedro", "TI", 5500, 28),
    (4, "Ana", "Vendas", 4000, 22),
    (5, "Carlos", "TI", 7000, 35)
]

df = spark.createDataFrame(dados, ["id", "nome", "depto", "salario", "idade"])

print("=" * 60)
print("OPERAÇÕES COM DATAFRAMES")
print("=" * 60)

print("\n📊 Dados completos:")
df.show()

print("\n🔹 SELECT - Selecionar colunas:")
df.select("nome", "salario").show()

print("\n🔹 FILTER - Filtrar:")
df.filter(col("salario") > 5000).show()

print("\n🔹 GROUP BY - Agrupar:")
df.groupBy("depto").count().show()

print("\n🔹 AGREGAÇÕES - Por departamento:")
df.groupBy("depto").agg(
    avg("salario").alias("salario_medio"),
    max("salario").alias("salario_max"),
    min("salario").alias("salario_min")
).show()

print("\n🔹 ORDER BY - Ordenar:")
df.orderBy(col("salario").desc()).show()

print("\n🔹 WITH COLUMN - Adicionar coluna:")
df.withColumn("salario_novo", col("salario") * 1.1).show()

spark.stop()

