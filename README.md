# 🎨 FauxFinder: Real vs Fake Art Detection

Welcome to **FauxFinder**, a cutting-edge application designed to classify images as **real art** or **AI-generated art** using advanced deep learning models. This project is part of a **course project** and leverages state-of-the-art models like **Custom CNN**, **MobileNetV1**, and **MobileNetV2** to provide accurate predictions. The app is deployed on **Streamlit Cloud**, making it accessible to users worldwide.

---
## File Hierarchy

### 1. **Source Code**
- **`DCGAN.ipynb`**: Contains the source code for training the **DCGAN** model to generate fake art images based on real art images.
- **`CNN and Pre-trained Models.ipynb`**: Contains the source code for training and fine-tuning **CNN** models, including **MobileNetV1** and **MobileNetV2**, for art image classification.

### 2. **App Deployment**
- **`app.py`**: Contains the source code for the deployed **web application** that uses the trained models to classify real vs. fake art images.

### 3. **Model Files**
- **`MobileNetV1_finetuned_models.keras`**: The fine-tuned **MobileNetV1** model for art image classification.
- **`MobileNetV2_finetuned_models.keras`**: The fine-tuned **MobileNetV2** model for art image classification.
- **`my_cnn.keras`**: The custom-trained **CNN** model for art image classification.

### 4. **Literature Review**
- **`Literature Review Folder/`**: Contains **research papers** that were reviewed as part of the project.
- **`literature_review_summary.pdf`**: Contains a **summary** of all the research papers that were reviewed.

### 5. **Images**
- **`images/`**: Contains images used in the final report and related visualizations.

### 6. **Extra Files**
- **`.idea/`**: Contains configuration files for the **IDE** (not essential for the project but required for the development environment).
- **`.gitattribute`**: Git configuration file for handling special file attributes.
- **`requirements.txt`**: Contains the list of **Python dependencies** required to run the project.
- **`LICENSE`**: The **license** file for this repository.
- **`README.md`**: This file, providing an overview of the project and the repository structure.
- **`demo.gif`**: A **demonstration** of the app or a visual showing the functionality of the project.
---

## 🚀 Introduction & Objective

The **FauxFinder** project aims to distinguish between **real art** and **AI-generated art** using deep learning models. With the rise of AI-generated art, this tool provides a reliable way to identify whether an artwork is created by a human or an AI. The app allows users to upload images and receive predictions with confidence scores, helping them understand the nature of the artwork.

The primary objective is to provide an **easy-to-use interface** for classifying art while maintaining high accuracy and interpretability. The app also allows users to select from multiple models for classification.

---
## 🎯 Features

- **Real vs Fake Art Classification**: Predicts whether an image is real art or AI-generated.
- **Model Selection**: Choose between three models:
  - **Custom CNN (85% Accuracy)**
  - **MobileNetV1 (95% Accuracy)**
  - **MobileNetV2 (92% Accuracy)**
- **Confidence Scores**: Displays the model's confidence level for each prediction.
- **Interactive UI**: User-friendly interface with dynamic background, progress bars, and clear visual feedback.
---

## 🧑‍💻 Technologies Used

- **Python** for backend development.
- **TensorFlow/Keras** for building and training deep learning models.
- **Streamlit** for building the web interface.
- **PIL/OpenCV** for image processing.
- **NumPy** for numerical computations.
---

## 📓 Kaggle Dataset

**Kaggle Dataset Link**: [Access Here](https://www.kaggle.com/datasets/doctorstrange420/real-and-fake-ai-generated-art-images-dataset)

---

# 🌐 Deployed Application

The tool is deployed on **Streamlit Cloud**, making it accessible to users worldwide.

**Streamlit App Link**: [Live Running App](https://fauxfinder-real-vs-fake-art-detection.streamlit.app/)

## Preview

![FauxFinder Demo](https://github.com/Kaleemullah-Younas/FauxFinder-Real-vs-Fake-Art-Detection/blob/main/demo.gif)  

---
---

## 🛠️ How to Run the Project

### From GitHub

1. **Fork the Repository**:  
   - Click the **Fork** button at the top-right corner of the repository.
2. **Clone the Repository**:  
   ```bash
   https://github.com/Kaleemullah-Younas/FauxFinder-Real-vs-Fake-Art-Detection.git
   ```
3. **Install Dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the App**:  
   ```bash
   streamlit run app.py
   ```
5. Open the local URL (http://localhost:8501) in your browser to access the app.

---
## 🤝 Contribute
We welcome contributions from the community! Feel free to fork the repository, submit issues, and create pull requests to enhance the project.

### 💻 How to Contribute

1. **Fork the Repository** on GitHub.  
2. **Clone Your Forked Repository**:  
   ```bash
   https://github.com/Kaleemullah-Younas/FauxFinder-Real-vs-Fake-Art-Detection.git
   ```
3. **Create a New Branch**:  
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make Your Changes and Commit**:  
   ```bash
   git commit -m "Add your message here"
   ```
5. **Push Changes to Your Fork**:  
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request**:  
   Open a pull request from your branch to the original repository's `main` branch.

---
## 📄 License

This project is licensed under the [license](LICENSE).

---
## 🌟 Acknowledgments
 
- **Faculty Advisors**: Thanks to our professors for their invaluable guidance throughout this project.  
- **Streamlit Community**: For resources and support in app deployment.  

