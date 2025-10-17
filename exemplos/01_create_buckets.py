import boto3
from botocore.exceptions import ClientError

# --- Configuração do cliente MinIO ---
s3_client = boto3.client(
    's3',
    endpoint_url='http://minio:9000',           # endpoint dentro do container
    aws_access_key_id='minioadmin',             # credenciais do docker-compose.yml
    aws_secret_access_key='minioadmin',         # credenciais do docker-compose.yml
    region_name='local'
)

# --- Cria buckets no MinIO ---
def create_buckets():
    buckets_to_create = ["landing-zone", "bronze-zone", "silver-zone", "gold-zone"]

    for bucket in buckets_to_create:
        try:
            s3_client.create_bucket(
                Bucket=bucket,
                CreateBucketConfiguration={'LocationConstraint': 'local'}
            )
            print(f"✅ Bucket '{bucket}' criado com sucesso.")
        except Exception as e:
            print(f"⚠️ Erro ao criar bucket '{bucket}': {e}")

if __name__ == "__main__":
    create_buckets()
