# 🐔 Chicken Disease Classification – End-to-End Project

![Build Status](https://img.shields.io/github/actions/workflow/status/AdMub/Chicken-Disease-Classification-End-to-End-Project/main.yml?branch=main&label=CI%2FCD%20Build&logo=github)  
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)   
![AWS](https://img.shields.io/badge/Deployed%20on-AWS-orange?logo=amazon-aws)  
![MLflow](https://img.shields.io/badge/MLflow-Tracking%20Enabled-blue?logo=mlflow)  
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)  
![License](https://img.shields.io/github/license/AdMub/Text-Summarization-NLP-End-to-End-Project) 

---

## 📌 Project Overview

Poultry farming is one of the most important agricultural practices worldwide, providing protein and livelihood for millions of people. However, poultry diseases like **Coccidiosis** pose a major threat to healthy chicken production.  

**Coccidiosis** is a parasitic disease caused by protozoa of the genus *Eimeria*. It affects the intestinal tract of chickens, leading to symptoms such as diarrhea, weight loss, reduced egg production, and even death in severe cases. Early detection is crucial to prevent economic loss and improve food security.

This project provides an **AI-powered solution** using **Deep Learning (VGG16 pre-trained model)** to automatically classify chicken images into:
- ✅ **Healthy**
- ❌ **Coccidiosis Infected**

By integrating **CI/CD pipelines**, **GitHub Actions**, **DVC (Data Version Control)**, and a **Flask Web App**, this project demonstrates a full-stack **MLOps workflow** for real-world deployment.

---

## 🚀 Features

- 📂 **Data Ingestion** 
- 🧠 **Model Building** – VGG16 pre-trained model fine-tuned for classification  
- 🔄 **Training Pipeline** – Includes callbacks, checkpoints, and logging  
- 📊 **Evaluation** – Reports model performance with metrics  

  Example Output:
  ```json
  {
      "loss": 1.2301383018493652,
      "accuracy": 0.9568965435028076
  }


---

## ⚙️ Key Features

- ⚙️ **Custom Exception Handling** – With `BoxValueError` for robust error tracking  
- 📝 **Logger** – Centralized logging for all project components  
- 🔗 **CI/CD** – Continuous integration & deployment using GitHub Actions  
- 📦 **DVC** – Data & model version control for reproducibility  
- 🌐 **Web App** – Flask application with HTML, CSS, and JavaScript (Home, Form, Result pages placeholders included)  

---

## 📁 Project Structure

```php
Chicken-Disease-Classification-End-to-End-Project
│── .dvc/ # DVC metadata
│── artifacts/ # Stored models, metrics, etc.
│── config/ # YAML configuration files
│── datasets/ # Raw and processed datasets
│── logs/ # Training & pipeline logs
│── research/ # Experiment notebooks
│── src/ # Source code
│ ├── components/ # Data ingestion, training, evaluation, etc.
│ ├── config/
│ ├── constants/
│ ├── entity/
│ ├── logging/
│ ├── pipeline/
│ ├── utils/
│ └── init.py
│── static/ # CSS, JS files for web app
│── templates/ # HTML templates (home.html, form.html, result.html)
│── app.py # Flask application entry point
│── .github/ # GitHub workflows (CI/CD)
│── .gitignore
│── .dvcignore
│── README.md
```

--

## 🖼️ Screenshots
 
**Home** – Project introduction

<img width="1901" height="906" alt="home" src="https://github.com/user-attachments/assets/84a1a41c-2c2a-476d-98c9-0769d8b368d3" />



**Form** - Upload chicken image for prediction

<img width="1907" height="913" alt="form" src="https://github.com/user-attachments/assets/eb279823-98a7-4efd-82b0-116b5704ac37" />



**Result** - Displays prediction result

<img width="1920" height="911" alt="coccidiosis" src="https://github.com/user-attachments/assets/f921742a-4c73-4d21-be4e-3cebad0d45c7" />



---

## ⚙️ Tech Stack

- **Deep Learning**: TensorFlow / Keras (VGG16 Pre-trained Model)  
- **MLOps Tools**: DVC, GitHub Actions, Logging, Custom Exception  
- **Web Framework**: Flask (HTML, CSS, JavaScript frontend)  
- **Version Control**: Git, GitHub  
- **Deployment Ready**: CI/CD pipeline  

---

## 📊 Model Performance

| Metric    | Value   |
|-----------|---------|
| Loss      | 1.2301  |
| Accuracy  | 95.69%  |

---

## 🖥️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/AdMub/Chicken-Disease-Classification-End-to-End-Project.git
   cd Chicken-Disease-Classification-End-to-End-Project
   ```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

```

3. **Install dependencies**
```bash
pip install -r requirements.txt

```

4. **Run DVC pipeline**
```bash
dvc repro

```

5. **Start the Flask app**
```bash
python app.py

```

6. **Open in browser**
```bash
http://127.0.0.1:8080


```


## 🐳 Docker Setup

Build and run backend in Docker:
```bash
docker build -t chicken-disease-classifier .
docker run -p 8080:8080 chicken-disease-classifier
```

---

## ⚡ CI/CD (GitHub Actions)

This project uses **GitHub Actions** for automation:
- ✅ Code linting & testing
- 🐳 Build & push Docker image
- ☁️ Deploy to AWS

Workflow file: `.github/workflows/main.yml`

<img width="1433" height="437" alt="CI-CD" src="https://github.com/user-attachments/assets/7d1269ae-5b8f-4377-a392-f62845571870" />


---

## 📜 License

This project is licensed under the [MIT License](LICENSE) – see the LICENSE file for details.


---

## ✨ Acknowledgments

- TensorFlow & Keras for deep learning framework
- DVC for experiment tracking and reproducibility
- GitHub Actions for CI/CD automation
- Poultry farmers & veterinary experts for inspiring this solution

  ---

## 👨‍💻 Author  

**Mubarak Adisa**  
- 🎓 Civil Engineering + Computer Science (Data Science & AI Focus)  
- 🔗 GitHub: [AdMub](https://github.com/AdMub)  
- 💼 LinkedIn: [Mubarak Adisa](https://www.linkedin.com/in/mubarak-adisa-334a441b6/)  
