import os
import json

os.environ["TRANSFORMERS_CACHE"] = "/tmp/"
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from transformers import TextClassificationPipeline


id2label = {0: "NEGATIVE", 1: "POSITIVE"}
label2id = {"NEGATIVE": 0, "POSITIVE": 1}

model = AutoModelForSequenceClassification.from_pretrained(
    "model/",
    num_labels=2,
    id2label=id2label,
    label2id=label2id,
)

tokenizer = AutoTokenizer.from_pretrained("prajjwal1/bert-tiny")


def classify(request, message):
    print(request)
    text = json.loads(request["body"])["text"]

    pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer)
    result = pipe(text)
    response = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(result),
    }
    return response
