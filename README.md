# 🖼️ Image Caption Generator

An end-to-end deep learning-based web application that generates descriptive captions for uploaded images. This project integrates Convolutional Neural Networks (ResNet50) for visual feature extraction and Recurrent Neural Networks (LSTM) for generating natural language descriptions using the **Flickr8k** dataset.

---

## 🚀 Objective

The main goal of this project is to develop a model that can interpret and describe the content of images using natural language. It combines visual understanding from CNNs with sequence modeling from RNNs to generate accurate and contextually meaningful captions.

---

## 🧠 How It Works

### 📷 ResNet50 for Image Feature Extraction
- **Deep Architecture:** A 50-layer deep residual network that mitigates vanishing gradients.
- **Purpose:** Extracts high-dimensional visual features from the input image.
- **Output:** Feature vector representing the visual content.

### 📝 LSTM for Caption Generation
- **Sequence Modeling:** Designed for handling time series and long-range dependencies.
- **Input:** Feature vector from ResNet50 + embedded previous words.
- **Output:** Generates caption word-by-word in a grammatically coherent way.

### 🔗 Integration Workflow

1. **Input Image → ResNet50**
2. **Extracted Features → LSTM**
3. **LSTM → Natural Language Caption**

---

## 🌟 Key Features

- 📌 End-to-end deep learning architecture
- 🧠 Combines CNN (ResNet50) + RNN (LSTM)
- 🖼️ Accepts user-uploaded images and returns a descriptive caption
- 🌐 Deployed using Flask web framework
- 📷 Trained using the **Flickr8k** dataset

---

## 📂 Dataset & Model

- 📁 **Dataset:** [Flickr8k Image Captioning Dataset](https://www.kaggle.com/datasets/adityajn105/flickr8k)
  - Contains 8,000 images with 5 captions each
- 🧠 **Model Architecture:**
  - ResNet50 (feature extraction)
  - LSTM (caption generation)
- 💾 Model trained and saved using Kaggle Notebooks

---

## ✨ Novelty

- 🧩 **CNN + RNN Integration:** Harmoniously combines image processing with text generation.
- ⚙️ **End-to-End Training:** Learns both visual features and their linguistic associations.
- 🔭 **Planned Enhancements:** Attention mechanism for improved focus and accuracy.

---

## 🧪 Future Work

- 🔍 **Incorporate Attention Mechanisms:** Focus on different regions of the image per word.
- 📚 **Enhance Vocabulary & Dataset:** Expand training data and word corpus.
- 🔁 **Experiment with Transformers:** Improve performance using modern architectures.

---

## 🌐 Website Preview

A Flask-based interface where users can upload an image and receive a generated caption in real time.

---

## ⚖️ Ethics

- 🔒 **Privacy:** Images used respect data privacy rights.
- ⚖️ **Bias Mitigation:** Conscious effort to reduce dataset and model biases.
- 📄 **Transparency:** Documented model architecture, training steps, and limitations.

---

## 📎 Tech Stack

- Python
- Keras / TensorFlow
- ResNet50 + LSTM
- Flask
- Jupyter / Kaggle Notebooks

---

## 👨‍💻 Author

**Jyothula Bhaskar**  
B.Tech in Computer Science & Engineering (AI & ML)  
[LinkedIn](https://www.linkedin.com/in/bhaskar-jyothula-974bbb271/) | [Hugging Face](https://huggingface.co/Bhaskar2611) | [GitHub](https://github.com/Bhaskarjyothula) | [Kaggle](https://www.kaggle.com/bhaskarjyothula)


---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
