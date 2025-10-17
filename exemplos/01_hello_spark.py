"""
Hello Spark - Primeiro Programa
================================
"""

from pyspark.sql import SparkSession

# Criar SparkSession
print("🚀 Iniciando Spark...")
spark = SparkSession.builder \
    .appName("HelloSpark") \
    .master("local[*]") \
    .getOrCreate()

print(f"✅ Spark {spark.version} iniciado!")

# Criar dados simples
dados = [
    ("João", 25, 5000),
    ("Maria", 30, 6000),
    ("Pedro", 28, 5500)
]

# Criar DataFrame
df = spark.createDataFrame(dados, ["nome", "idade", "salario"])

print("\n📊 DataFrame:")
df.show()

print("\n🔍 Filtro - Salário > 5000:")
df.filter(df.salario > 5000).show()

print("\n📈 Estatísticas:")
df.describe().show()

# Encerrar
spark.stop()
print("\n✅ Finalizado!")

