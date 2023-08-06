config = {}

import click

MLFLOW_TRACKING_URI = "MLFLOW_TRACKING_URI"
IAM_URI = "IAM_URI"

def set_env(env):
    if env == "stg": 
        config[MLFLOW_TRACKING_URI] = "http://35.238.159.24:5000"
        config[IAM_URI] = "https://iam-dhuo-data-stg.br.engineering"
    else:
        click.echo(f"environment {env} not implemented")

# MLFLOW_TRACKING_URI=https://mlflow-dhuo-data-prd.br.engineering