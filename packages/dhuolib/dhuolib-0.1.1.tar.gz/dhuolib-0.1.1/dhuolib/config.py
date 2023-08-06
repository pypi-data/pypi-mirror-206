config = {}


def set_env(env):
    config["MLFLOW_TRACKING_URI"] = 


    "MLFLOW_TRACKING_URI": "http://35.238.159.24:5000",
    "AWS_ACCESS_KEY_ID": "ZPmLIAFFe3zNafR5",
    "AWS_SECRET_ACCESS_KEY": "lJXFYMz9ZeyoH43uDJJFDqW9uUx5lhsV",
    "AWS_DEFAULT_REGION": "us-east-1",
    "BUCKET_NAME": "mlflow-bucket",
    "BUCKET_FOLDER": "mlflow",
    "S3_ENDPOINT_URL": "=localhost:9000",
    "IAM_URI": "https://iam-dhuo-data-stg.br.engineering"
}



# MLFLOW_TRACKING_URI=https://mlflow-dhuo-data-prd.br.engineering








def set_env(env):
    if env == 'stg':
        ENV =