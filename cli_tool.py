import subprocess
import click
import os 

@click.group()
def cli():
    pass

@cli.command()
def train_local():
    """Run the method for training on local machine."""
    print("Running training on local machine...")
    subprocess.run(["/usr/bin/python3", "/home/ravneet-singh/first/titanic/modeling/train.py"], check=True)

@cli.command()
def train_deployment():
    """Run the method for training on Docker."""
    print("Running training on Docker...")
    try:
        subprocess.run([
            "docker", "run", "-it", "--rm", 
            "-v", "/home/ravneet-singh/machine-learning/titanic-survival-prediction:/app",
            "my-titanic-training-image",
            "python3", "/apps/titanic/modeling/train.py"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running training: {e}")



@cli.command()
def service_local():
    """Start the local server for the model endpoint (FastAPI endpoint)."""
    print("Starting local server for model endpoint...")
    subprocess.run(["uvicorn", "api.app:app", "--host", "127.0.0.1", "--port", "8000"], check=True)

@cli.command()
def service_deploy():
    """Run the method for model serving on Docker."""
    print("Running model serving on Docker...")
    subprocess.run([
        "docker", "run", "--rm", "-p", "5000:5000", 
        "-v", "/home/ravneet-singh/machine-learning/titanic-survival-prediction/api:/app", 
        "my-fastapi-app"
    ], check=True)

if __name__ == "__main__":
    cli()
