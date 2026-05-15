# 🎓 Student Performance Prediction AI

An advanced Machine Learning web application built using Streamlit that predicts student GPA and academic performance using various educational and behavioral factors.

---

# 🚀 Features

✅ Predicts Student GPA using Machine Learning
✅ Modern futuristic Streamlit dashboard UI
✅ Interactive Gauge and Analytics Charts
✅ Lottie Animations for premium appearance
✅ AI-based Recommendations for students
✅ Real-time prediction system
✅ Clean and responsive design
✅ Data visualization using Plotly
✅ Deployable on Streamlit Cloud

---

# 🧠 Machine Learning Models Used

The dataset was trained on multiple regression models:

| Model                   | Performance |
| ----------------------- | ----------- |
| Linear Regression       | Good        |
| Decision Tree Regressor | Better      |
| Random Forest Regressor | Best        |

The best-performing model was selected and saved as:

```plaintext
student_performance_model.pkl
```

---

# 📂 Dataset Used

Dataset Name:

Student Performance Dataset

Source:

Kaggle Dataset

Features used:

* Age
* Gender
* Parental Education
* Study Time Weekly
* Absences
* Tutoring
* Parental Support
* Extracurricular Activities
* Sports Participation
* Music Activities
* Volunteering
* Previous Academic Performance

Target Variable:

```plaintext
GPA
```

---

# 🛠️ Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Streamlit    | Web Application Framework |
| Scikit-learn | Machine Learning          |
| Pandas       | Data Processing           |
| NumPy        | Numerical Computation     |
| Plotly       | Interactive Charts        |
| Joblib       | Model Saving              |
| Lottie       | UI Animations             |

---

# 📊 Application Dashboard

The application contains:

* GPA Prediction Meter
* Student Analytics Dashboard
* AI Recommendations
* KPI Cards
* Modern Responsive UI

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Bushra2708/Student-Performance-Perdictor
```

Go to project folder:

```bash
cd student-performance-ai
```

Install required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

# 📦 Project Structure

```plaintext
student-performance-ai/
│
├── app.py
├── student_performance_model.pkl
├── requirements.txt
├── README.md
└── dataset/
```

---

# 📈 Model Evaluation

Evaluation metrics used:

* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

The project was trained and tested using train-test split methodology.

---

# 🌐 Deployment

The application is deployed using:

Streamlit Community Cloud

#Live Link:
https://student-performance-perdictor-txwcywgjtmfjtbgrdxtxch.streamlit.app/
