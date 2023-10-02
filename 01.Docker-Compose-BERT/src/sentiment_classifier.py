import torch
from torch import nn
from transformers import BertModel

MODEL_NAME = 'bert-base-cased'

class SentimentClassifier(nn.Module):
    
    def __init__(self, n_classes, weight_decay=0.0001):
        super(SentimentClassifier, self).__init__()
        self.bert = BertModel.from_pretrained("bert-base-cased", return_dict=False)
        self.bn = nn.BatchNorm1d(self.bert.config.hidden_size)
        self.drop_bert = nn.Dropout(p=0.3)
        self.out = nn.Linear(self.bert.config.hidden_size, n_classes)
        self.relu = nn.ReLU()
        self.drop_out = nn.Dropout(p=0.3)
        self.sigmoid = nn.Sigmoid()

        self.weight_decay = weight_decay
        
    def forward(self, input_ids, attention_mask,return_dict=False):
        _, pooled_output = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        output = self.bn(pooled_output)
        output = self.drop_bert(output)
        output = self.out(output)
        output = self.relu(output)
        output = self.drop_out(output)
        output = self.sigmoid(output)

        return output
    
    
    def loss_fn(self, outputs, targets):
        criterion = nn.BCELoss()
        # Calculate L2 regularization loss
        l2_loss = torch.tensor(0.0).to(outputs.device)
        for name, param in self.named_parameters():
            if 'weight' in name:
                l2_loss += torch.norm(param, p=2)
        return criterion(outputs, targets) + self.weight_decay * l2_loss