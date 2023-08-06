# cli.py

import logging
import click
import os
from dhuolib.auth.login import do_login
from dotenv import load_dotenv
from dhuolib import config


load_dotenv() 


@click.group()
def main():
    """Library for data science on DHuO Data"""
    


@main.command()
@click.option('--email', prompt=True, help='Your DHuO Data email')
@click.option('--password', prompt=True, help='Your DHuO Data password', 
            hide_input=True, confirmation_prompt=False)
@click.option("--env", 
            help="Specify environment",
            default="prd",
            type=click.Choice(["prd", "dev", "stg"]))
def login(email, password, env):
    """Provides user authentication"""

    click.echo(f"Efetuando login em {env}")

    config.set_env(env)

    try: 
        if env == "stg":
            do_login(email, password)
            click.echo(f"Seja bem-vindo ao DHuO Data {email}")

    except Exception as e:
        # logging.exception("Logon error") 
        #        
        click.echo("Erro ao efetuar login: " + str(e))
