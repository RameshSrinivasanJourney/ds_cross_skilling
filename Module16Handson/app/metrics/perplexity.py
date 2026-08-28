import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
)


MODEL_NAME = (
    "distilgpt2"
)


class PerplexityCalculator:

    def __init__(
        self,
        model_name: str = MODEL_NAME,
    ) -> None:

        self.tokenizer = (
            AutoTokenizer.from_pretrained(
                model_name
            )
        )

        self.model = (
            AutoModelForCausalLM.from_pretrained(
                model_name
            )
        )

        self.model.eval()

    def calculate(
        self,
        text: str,
    ) -> float:

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
        )

        with torch.no_grad():

            outputs = self.model(
                **inputs,
                labels=inputs["input_ids"],
            )

        loss = outputs.loss

        return torch.exp(
            loss
        ).item()