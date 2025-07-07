from django.shortcuts import render
import os
from django.conf import settings
import numpy as np
import joblib
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

model_path = os.path.join(settings.BASE_DIR, 'model', 'insurance.pkl')
model = joblib.load(model_path)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, "Invalid username or password") 
            return render(request, 'login.html')  
    return render(request, 'login.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already taken"})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect("home")

    return render(request, "signup.html")

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

@login_required(login_url='login')
def prediction(request):
    if request.method == 'POST':
        try:
            print("POST data:", request.POST)
            age = int(request.POST.get('age'))
            sex = int(request.POST.get('sex'))
            bmi = float(request.POST.get('bmi'))
            children = int(request.POST.get('children'))
            smoker = int(request.POST.get('smoker'))
            region = int(request.POST.get('region')) - 1 

            input_data = np.array([[age, sex, bmi, children, smoker, region]])

            prediction = model.predict(input_data)[0]
            prediction = round(float(prediction), 2)

            return render(request, 'prediction.html', {'output': prediction})

        except Exception as e:
            print("Error during prediction:", e)
            return render(request, 'prediction.html', {'output': 'Invalid input. Please try again.'})

    return render(request, 'prediction.html')

def logout_view(request):
    logout(request)
    return redirect('home') 