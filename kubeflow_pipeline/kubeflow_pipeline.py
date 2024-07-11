import os
import kfp
import kfp.dsl as dsl
from kfp.dsl import component, pipeline

@component(base_image='python:3.8')
def train_model():
    import subprocess
    subprocess.run(['python', '/home/ravneet-singh/machine-learning/titanic-survival-prediction/titanic/modeling/train.py'], check=True)

@pipeline(
    name='Model Training Pipeline',
    description='An example pipeline that trains a scikit-learn model and logs it to MLflow.'
)
def training_pipeline():
    train_task = train_model()

if __name__ == '__main__':
    # Ensure the output directory exists
    os.makedirs('kubeflow_pipeline', exist_ok=True)
    kfp.compiler.Compiler().compile(training_pipeline, 'kubeflow_pipeline/training_pipeline.yaml')
