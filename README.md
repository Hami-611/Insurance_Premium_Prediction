## 🏥 Insurance Premium Prediction

A full-stack web application that predicts insurance premium costs based on user inputs such as age, BMI, region, smoking status, and more. The backend is powered by a trained **Random Forest Regressor** integrated into a Django application.

---

### 🔍 Features

* 🎯 Predicts insurance premiums using Random Forest Regression
* ✅ Clean Django frontend with Bootstrap UI
* 💾 Real-time prediction without page reloads
* 🧠 Trained on structured insurance dataset
* 🚀 Deployed on Render 
* 🔒 Basic form validation and CSRF protection

---

### 🛠️ Tech Stack

| Layer      | Tools Used                                          |
| ---------- | --------------------------------------------------- |
| ML Model   | Python, Pandas, Scikit-learn, RandomForestRegressor |
| Backend    | Django, Django Templates, `joblib`                  |
| Frontend   | HTML, CSS, Bootstrap                                |
| Deployment | Render (Backend), PostgreSQL (optional)             |
| Dev Tools  | Git, VS Code, Postman, pip                          |

---

### 📈 How It Works

1. User enters details like age, BMI, region, smoker status, etc.
2. Data is passed to the backend view.
3. The trained Random Forest model (`model.pkl`) makes a prediction.
4. Result is returned and displayed on the same page.

---

### ⚙️ Installation

#### 🔧 1. Clone the Repository

```bash
git clone https://github.com/Hami-611/Insurance_Premium_Prediction.git
cd insurance
```

#### 📦 2. Create Virtual Environment & Install Requirements

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux

pip install -r requirements.txt
```

#### 🧠 3. Train or Load Model

You can use the pre-trained model or train your own:

#### 🚀 4. Run the Server

```bash
python manage.py runserver
```

---

### 🌐 Live Demo

> [https://insurance-premium-prediction-ti26.onrender.com](https://insurance-premium-prediction-ti26.onrender.com)

---

### 🧪 Sample Input

| Feature  | Example Value                |
| -------- | ---------------------------- |
| Age      | 29                           |
| BMI      | 27.5                         |
| Children | 2                            |
| Smoker   | Yes                          |
| Region   | southeast                    |

---


### 📌 Deployment Notes

* Django backend deployed to **Render**
* Set `DATABASE_URL` and `SECRET_KEY` in Render’s environment variables or use SQLite for local
* Model file (`model.pkl`) is loaded using `joblib`

---

### 📜 License

This project is open-source under the MIT License.

