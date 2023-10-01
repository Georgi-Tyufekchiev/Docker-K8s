from transformers import BertTokenizer
import torch
from sentiment_classifier import SentimentClassifier

def predict(review_text : str) -> str: 
    MODEL_NAME = 'bert-base-cased'
    tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
    MAX_LEN = 400
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = SentimentClassifier(2)
    model = model.to(device)

    class_names = ['positive', 'negative']
    model.load_state_dict(torch.load("src/model/best_model_state.bin", map_location=torch.device(device)))
    model.eval()
    encoded_review = tokenizer.encode_plus(
        review_text,
        max_length=MAX_LEN,
        add_special_tokens=True,
        return_token_type_ids=False,
        padding="max_length",
        return_attention_mask=True,
        return_tensors='pt',
    )
    input_ids = encoded_review['input_ids'].to(device)
    attention_mask = encoded_review['attention_mask'].to(device)

    output = model(input_ids, attention_mask)
    _, prediction = torch.max(output, dim=1)

    # print(f'Review text: {review_text}')
    return class_names[prediction]