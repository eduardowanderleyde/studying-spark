"""
Leitura de Arquivos CSV
========================
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("LerCSV") \
    .master("local[*]") \
    .getOrCreate()

print("=" * 60)
print("LENDO ARQUIVO CSV")
print("=" * 60)

# Ler CSV
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("dados/exemplo.csv")

print("\n📄 Dados do CSV:")
df.show()

print("\n📋 Schema:")
df.printSchema()

print("\n📊 Estatísticas:")
df.describe().show()

print("\n🔍 Filtro - idade > 25:")
df.filter(df.idade > 25).show()

# Salvar resultado
print("\n💾 Salvando em Parquet...")
df.write.mode("overwrite").parquet("dados/output.parquet")
print("✅ Salvo!")

spark.stop()

