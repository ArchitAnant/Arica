import torch
import torch.nn as nn
import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
import json
import pickle

stemmer = LancasterStemmer()

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return torch.softmax(x, dim=1)

def load_data():
    with open("model_ml/dataset.json") as file:
        data = json.load(file)

    try:
        with open("model_ml/model/data.pickle", "rb") as f:
            words, labels, training, output = pickle.load(f)
    except:
        words = []
        labels = []
        docs_x = []
        docs_y = []

        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                words.extend(wrds)
                docs_x.append(wrds)
                docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

        words = [stemmer.stem(w.lower()) for w in words if w != "?"]
        words = sorted(list(set(words)))

        labels = sorted(labels)

        training = []
        output = []

        out_empty = [0 for _ in range(len(labels))]

        for x, doc in enumerate(docs_x):
            bag = []

            wrds = [stemmer.stem(w.lower()) for w in doc]

            for w in words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)

            output_row = out_empty[:]
            output_row[labels.index(docs_y[x])] = 1

            training.append(bag)
            output.append(output_row)

        training = np.array(training)
        output = np.array(output)

        with open("model_ml/model/data.pickle", "wb") as f:
            pickle.dump((words, labels, training, output), f)

    return words, labels, training, output

words, labels, training, output = load_data()

input_size = len(training[0])
hidden_size = 8
output_size = len(output[0])

model = NeuralNet(input_size, hidden_size, output_size)

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.5)

for epoch in range(9000):
    inputs = torch.Tensor(training).float()
    targets = torch.Tensor(output).float()

    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()

    if (epoch+1) % 100 == 0:
        with torch.no_grad():
            predicted = torch.argmax(outputs, dim=1)
            actual = torch.argmax(targets, dim=1)
            correct = (predicted == actual).sum().item()
            total = actual.size(0)
            accuracy = correct / total
            print(f'Epoch [{epoch+1}/2000], Accuracy: {accuracy * 100:.2f}%')

torch.save(model.state_dict(), "model_ml/model/model.pth")
