import datasets
from typing import cast
from transformers import AutoTokenizer, BertForSequenceClassification, TrainingArguments, Trainer

dataset = datasets.load_dataset("csv", data_files="config/dataset.csv")
train_ds = cast(datasets.Dataset, dataset["train"])
unique_intents = list(set(train_ds["intent"]))
label_to_id = {label: i for i, label in enumerate(unique_intents)}
id_to_label = {i: label for i, label in enumerate(unique_intents)}
print(f"Unique intents loaded: {unique_intents}")
print(f"Label to ID mapping: {label_to_id}")
print(f"ID to label mapping: {id_to_label}")

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def tokenize_function(examples):
    return tokenizer(examples["phrase"], padding="max_length", truncation=True)

def tokenize_and_encode(examples):
    tokens = tokenizer(examples["phrase"], padding="max_length", truncation=True, max_length=32)
    tokens["label"] = label_to_id[examples["intent"]]
    return tokens

tokenized_dataset = train_ds.map(tokenize_function)
tokenized_dataset = train_ds.map(tokenize_and_encode)

tokenized_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "label"])

model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=len(label_to_id), id2label=id_to_label, label2id=label_to_id)
training_args = TrainingArguments(
    output_dir="output",
    per_device_train_batch_size=8,
    num_train_epochs=10,
    save_strategy="no",
    logging_steps=10,
    report_to="none"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset
)

trainer.train()
model.save_pretrained("output/model")
tokenizer.save_pretrained("output/tokenizer")