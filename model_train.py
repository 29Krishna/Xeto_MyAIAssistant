#intent based chatbot
import json
import numpy as np
import os 
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder 
import pickle

#load intents.json
with open("intents.json") as file:
    data = json.load(file)

# data preparation
training_sentencs = []
training_labels = []
labels = []
responses = []



for intent in data["intents"]:
    for pattern in intent["patterns"]:
        training_sentencs.append(pattern)
        training_labels.append(intent["tag"])
    responses.append(intent['responses'])

    if intent['tag'] not in labels:
        labels.append(intent['tag'])

#checking if data is loaded correctly or not
print("Training sentences:", training_sentencs)
print("Training labels:", training_labels)
print("Labels:", labels)

number_of_classes = len(labels)
print(number_of_classes)

# label encoding
label_encoder = LabelEncoder()
label_encoder.fit(training_labels)
training_labels = label_encoder.transform(training_labels)

#tokenization
vocab_size = 1000
max_len = 20
ovv_token = "<OOV>"
embedding_dimensions = 16

tokenizer = Tokenizer(num_words=vocab_size,oov_token = ovv_token)
tokenizer.fit_on_texts(training_sentencs)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(training_sentencs)
padded_sequences = pad_sequences(sequences,truncating = 'post', maxlen = max_len)

# Check tokenization output
print("Word Index:", word_index)
print("Sequences:", sequences)
print("Padded Sequences:", padded_sequences)


# model creation
model = Sequential()
model.add(Embedding(vocab_size,embedding_dimensions))
model.add(GlobalAveragePooling1D())
model.add(Dense(16,activation = "relu"))
model.add(Dense(16,activation = "relu"))
model.add(Dense(number_of_classes,activation = "softmax"))

#force build model
model.build(input_shape=(None, max_len))

#compile and summarize model
model.compile(loss = "sparse_categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])
model.summary()



#model training
history = model.fit(padded_sequences, np.array(training_labels), epochs = 1000)

model.save("chat_model.h5")

with open("tokenizer.pkl","wb") as f:
    pickle.dump(tokenizer,f, protocol = pickle.HIGHEST_PROTOCOL)

with open("label_encoder.pkl","wb") as encoder_file:
    pickle.dump(label_encoder, encoder_file , protocol = pickle.HIGHEST_PROTOCOL)

