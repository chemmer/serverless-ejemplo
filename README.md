# serverless-ejemplo
An example use case how to use serverless for Machine Learning. Model creation code stolen from https://huggingface.co/docs/transformers/tasks/sequence_classification. 

# Installation
1. [Install Python](https://letmegooglethat.com/?q=how+to+install+python)

## Serverless Function
1. Create a (free) [AWS Account](https://aws.amazon.com)
2. Install and configure the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
3. Install the [serverless](https://www.serverless.com/framework/docs-getting-started) framework

## Model creation
1. Install dependencies:
```console 
$ cd model_creation
$ pip install -r requirements.txt
```
2. Modify the Jupyter Notebook to your wishes
3. Create a new model and save it in serverless_function/model/

# Deployment
Run in the console
```console 
$ cd serverless_function
$ serverless deploy
```

# Usage
- Copy the URL output from the serverless deploy run
- Do a post request to the with a text parameter