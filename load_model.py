import torch
import torch.nn as nn
import numpy as np
import nltk
from nltk.stem.lancaster import LancasterStemmer
import json
import pickle
import random

PATH_TO_DATASET = "model_ml/dataset.json"
PATH_TO_DATAPKL = "model_ml/model/data.pickle"
PATH_TO_MODEL = "model_ml/model/model.pth"


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

# model = NeuralNet(input_size, hidden_size, output_size)

# criterion = nn.MSELoss()
# optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# model_path = PATH_TO_MODEL  # Path to your model file
# state_dict = torch.load(model_path)

# Set the model's state_dict using the loaded state_dict
# model.load_state_dict(state_dict)

# for epoch in range(2000):
#     inputs = torch.Tensor(training).float()
#     targets = torch.Tensor(output).float()

#     optimizer.zero_grad()
#     outputs = model(inputs)
#     loss = criterion(outputs, targets)
#     loss.backward()
#     optimizer.step()

#     if (epoch+1) % 100 == 0:
#         with torch.no_grad():
#             predicted = torch.argmax(outputs, dim=1)
#             actual = torch.argmax(targets, dim=1)
#             correct = (predicted == actual).sum().item()
#             total = actual.size(0)
#             accuracy = correct / total
#             print(f'Epoch [{epoch+1}/2000], Accuracy: {accuracy * 100:.2f}%')

# torch.save(model.state_dict(), "model_ml/model/model.pth")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    return bag

def chat(query):
    words, labels, _, _ = load_data()
    model = NeuralNet(input_size, hidden_size, output_size)
    model.load_state_dict(torch.load(PATH_TO_MODEL))
    model.eval()

    with torch.no_grad():
        bag = bag_of_words(query, words)
        inputs = torch.Tensor(bag).unsqueeze(0).float()
        outputs = model(inputs)
        results = outputs.numpy()[0]

    results_index = np.argmax(results)
    print(results[results_index])
    if results[results_index] > 0.85:
        tag = labels[results_index]
        with open("model_ml/dataset.json") as file:
            data = json.load(file)
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
                    output = random.choice(responses)
                    if tag == "FILE_CREATION":
                        output = random.choice(responses)
        return output
    else:
        return "supposed to be google"

# print(chat(input(": ")))
