from transformers import AutoTokenizer, BertForSequenceClassification
import torch
from utils.logger import Logger

class Brain:
    def __init__(self, model_path: str = "output/model", tokenizer_path: str = "output/tokenizer"):
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        self.model = BertForSequenceClassification.from_pretrained(model_path)
        self.model.eval()
        self.logger = Logger().get_logger()
        self.logger.info("Brain initialized with model and tokenizer.")
        

    def proccess_command(self, command: str):
        self.logger.info(f"Processing command: {command}")
        inputs = self.tokenizer(command, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_label_id = torch.argmax(logits, dim=1).item()
        intent = self.model.config.id2label[predicted_label_id]
        self.logger.info(f"Predicted intent: {intent} for command: {command}")
        return intent