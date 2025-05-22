# 🎓 Student Exam Performance Predictor

A lightweight Flask web app that predicts a student's **Math score** based on personal background and academic performance. The app is trained on historical exam data and provides real-time predictions through a web interface.

---

## 📽️ Demo

<div align = "centre">
<img src=https://github.com/user-attachments/assets/4e506785-588e-4ee9-b4d4-b709d16d5fa5 >
</img>
</div>
  
</div>

---

## 🚀 Features

- Predicts math scores based on:
  - Gender
  - Ethnicity
  - Parental education
  - Lunch type
  - Test prep course
  - Reading and writing scores
- User-friendly interface using **Bootstrap**
- Built with **Flask (Python 3.10.16)**
- Deployable using **Docker**

---
## Data Collection 
### 1) Problem statement
- This project understands how the student's performance (test scores) is affected by other variables such as Gender, Ethnicity, Parental level of education, Lunch and Test preparation course.


### 2) Data 
- Dataset Source - https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977
- The data consists of 8 column and 1000 rows.


## 🧠 Tech Stack

- **Frontend**: HTML, Bootstrap
- **Backend**: Flask (Python 3.10.16)
- **ML Libraries**: pandas, numpy, scikit-learn
- **Model Serialization**: dill

---


## ⚙️ Local Setup (Without Docker)

### 1. Clone the Repository

```
git clone https://github.com/S1000-bit/Student_Marks_Prediction.git
cd Student_Marks_Prediction
```

### 2. Create a virtual environment

```
python3.10 -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate.bat  # Windows 
```


## 🐳 With Docker

### 1.Build the Docker Image

```
docker build -t student-exam-predictor .
```

### 2.Run the Container

```
docker run -p 5000:5000 student-exam-predictor
```

## 📬 License

- This project is licensed under the MIT License.


