# 📚 Estudando Apache Spark com PySpark

Projeto de estudos do Apache Spark usando PySpark em container Docker.

## 🐳 Configuração Docker

Este projeto utiliza Docker Compose para rodar:
- **Jupyter Lab** com PySpark (Python 3.11)
- **MinIO** para armazenamento de objetos (S3-compatible)

### Como executar

```bash
docker-compose up -d
```

### Acessar serviços

- **Jupyter Lab**: http://localhost:8888 (senha: `password`)
- **Spark UI**: http://localhost:4050
- **MinIO**: http://localhost:9000

## 📁 Estrutura do Projeto

```
studying-spark/
├── dados/              # Arquivos de dados (CSV, etc)
├── exemplos/           # Scripts Python com exemplos
├── notebooks/          # Jupyter Notebooks
└── docker-compose.yml  # Configuração Docker
```

## 🚀 Exemplos

- `01_hello_spark.py` - Introdução ao Spark
- `02_dataframes.py` - Operações com DataFrames
- `03_spark_sql.py` - Consultas SQL no Spark
- `04_ler_csv.py` - Leitura e escrita de arquivos

## 💡 Tecnologias

- Apache Spark 3.x
- Python 3.11
- PySpark
- Jupyter Lab
- Docker
- MinIO

