from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
import json
from tensorflow.keras.applications import ResNet50
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

model = load_model('my_combined_model.h5',compile=False)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'model_data')

word_2_indices_path = os.path.join(DATA_DIR, 'word_2_indices.json')
indices_2_word_path = os.path.join(DATA_DIR, 'indices_2_word.json')

# Load word_2_indices dictionary
with open(word_2_indices_path, 'r') as f:
    word_2_indices = json.load(f)

# Load indices_2_word dictionary
with open(indices_2_word_path, 'r') as f:
    indices_2_word = json.load(f)

resnet = ResNet50(include_top=False, weights='imagenet', input_shape=(224, 224, 3), pooling='avg')
# Define a function to preprocess the image

def preprocess_image(img_path):
    im = img_path.resize((224, 224))
    im = np.array(im)
    im = np.expand_dims(im, axis=0)
    return im

def get_encoding(model, img):
    pred = model.predict(img).reshape(2048)
    return pred



def predict_captions(image):
    start_word = ["<start>"]
    while True:
        par_caps = [word_2_indices[i] for i in start_word]
        par_caps = sequence.pad_sequences([par_caps], maxlen=40, padding='post')
        preds = model.predict([np.array([image]), np.array(par_caps)])
        word_index = np.argmax(preds[0])
        print(word_index)
        word_pred = indices_2_word[str(word_index)]  # Convert index to string for dictionary lookup
        
        start_word.append(word_pred)
        
        if word_pred == "<end>" or len(start_word) > 40:
            break
            
    return ' '.join(start_word[1:-1])



# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route to handle the image upload and make predictions
@app.route('/predict', methods=['POST'])
def upload():
    if request.method == 'POST':
       f = request.files['image']
       
       img = Image.open(f)
       preprocess=preprocess_image(img)
       test_img= get_encoding(resnet, preprocess)
       print(test_img)
       Argmax_Search = predict_captions(test_img)  
       return jsonify({'caption': Argmax_Search})


if __name__ == '__main__':
    app.run(debug = False, threaded = False)
