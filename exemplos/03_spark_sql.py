"""
Spark SQL
=========
Usando SQL para consultar DataFrames
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkSQL") \
    .master("local[*]") \
    .getOrCreate()

# Criar DataFrame
dados = [
    (1, "João", "TI", 5000),
    (2, "Maria", "RH", 6000),
    (3, "Pedro", "TI", 5500),
    (4, "Ana", "Vendas", 4000),
    (5, "Carlos", "TI", 7000)
]

df = spark.createDataFrame(dados, ["id", "nome", "depto", "salario"])

# Registrar como tabela SQL
df.createOrReplaceTempView("funcionarios")

print("=" * 60)
print("SPARK SQL")
print("=" * 60)

print("\n1️⃣ SELECT básico:")
spark.sql("SELECT * FROM funcionarios").show()

print("\n2️⃣ WHERE:")
spark.sql("""
    SELECT nome, salario 
    FROM funcionarios 
    WHERE salario > 5000
""").show()

print("\n3️⃣ ORDER BY:")
spark.sql("""
    SELECT nome, salario 
    FROM funcionarios 
    ORDER BY salario DESC
""").show()

print("\n4️⃣ GROUP BY:")
spark.sql("""
    SELECT 
        depto,
        COUNT(*) as total,
        AVG(salario) as salario_medio
    FROM funcionarios
    GROUP BY depto
""").show()

print("\n5️⃣ CASE WHEN:")
spark.sql("""
    SELECT 
        nome,
        salario,
        CASE 
            WHEN salario < 5000 THEN 'Júnior'
            WHEN salario < 6000 THEN 'Pleno'
            ELSE 'Sênior'
        END as nivel
    FROM funcionarios
""").show()

spark.stop()

