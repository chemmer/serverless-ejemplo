FROM public.ecr.aws/lambda/python:3.10

RUN pip install --no-cache-dir transformers torch

COPY model ${LAMBDA_TASK_ROOT}/model
COPY handler.py ${LAMBDA_TASK_ROOT}

CMD [ "handler.classify" ]