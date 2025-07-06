### 📄 `README.md`

```markdown

# 🛡️ Insurance Prediction Web App

This is a Django-based web application that allows users to predict insurance expenses based on input features like age, sex, BMI, number of children, smoking habits, and region.

---

## 🚀 Features

- User authentication system
- Interactive prediction form
- Dynamic result rendering
- Static files handling via WhiteNoise
- Dockerized setup for easy deployment
- Environment variables support via `.env`

---

## 🗂️ Project Structure

mlproject/
│
├── insurance/          # Django project folder (settings, wsgi, urls)
├── home/               # Django app folder (static, templates, views)
├── staticfiles/        # Collected static files (generated)
├── manage.py
├── requirements.txt
├── .env
└── .gitignore

````

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/insurance.git
cd insurance
````

### 2. Create `.env` File

```env
DEBUG=True
SECRET_KEY=your-django-secret-key
```

---

## ⚙️ Collecting Static Files

Static files are managed using WhiteNoise. To collect them:

```bash
python manage.py collectstatic
```

They will be stored in the `/staticfiles/` directory.

---

## ✅ Dependencies

* Django >= 4.2
* python-dotenv
* whitenoise

You can install them using:

```bash
pip install -r requirements.txt
```

---

## 🧪 Running the Server Locally

```bash
python manage.py runserver
```

---

## 📌 Notes

* Do not commit `.env` or `staticfiles/` to Git.
* WhiteNoise is used to serve static files in production.
* Replace SQLite with PostgreSQL for production-level deployment.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👩‍💻 Author

Made with ❤️ by **Hamika Redrowthu**

```

```
