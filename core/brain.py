from transformers import AutoTokenizer, BertForSequenceClassification
import torch
from utils.logger import Logger

class Brain:
    def __init__(self, logger: Logger, model_path: str = "output/model", tokenizer_path: str = "output/tokenizer"):
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
        self.model = BertForSequenceClassification.from_pretrained(model_path)
        self.model.eval()
        self.logger = logger.get_logger()
        self.logger.info("Brain initialized with model and tokenizer.")
        

    def proccess_command(self, command: str):
        self.logger.info(f"Processing command: {command}")
        inputs = self.tokenizer(command, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits

        probs = torch.nn.functional.softmax(logits, dim=1)
        self.logger.info(f"Command probabilities: {probs}")
        if torch.max(probs) < 0.5:
            self.logger.warning(f"Low confidence in command processing: {command}")
            return {"intent": "unknown", "text": command}

        predicted_label_id = torch.argmax(logits, dim=1).item()
        intent = self.model.config.id2label[predicted_label_id]
        self.logger.info(f"Predicted intent: {intent} for command: {command}, confidence: {torch.max(probs).item()}")

        return {"intent": intent,
                "text": command
                }
    