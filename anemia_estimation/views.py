from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.hashers import check_password, make_password
import re
import os
import sys
import pandas as pd
from matplotlib import pyplot, pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn import linear_model, metrics, model_selection, svm
import csv
from django.templatetags.static import static

def login(request):
    msg=''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to home page or desired page
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'login.html')



def register(request):
    msg = ""
    if request.method == "POST":
        try:
            first_name = request.POST.get("first_name")
            middle_name = request.POST.get("middle_name", "")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            mobile_number = request.POST.get("mobile_number")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            
            # Check if passwords match
            if password != confirm_password:
                msg = "Passwords do not match"
            
            # Check if username is already taken
            elif User.objects.filter(username=username).exists():
                msg = "Username is already taken"
            
            # Check if email is already registered
            elif User.objects.filter(email=email).exists():
                msg = "Email is already registered"
            
            # Check if mobile number is already registered
            elif User.objects.filter(mobile_number=mobile_number).exists():
                msg = "Mobile number is already registered"
            
            else:
                # Hash the password
                hashed_password = make_password(password)

                # Create new user
                User.objects.create(
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    mobile_number=mobile_number,
                    password=hashed_password
                )
                msg = "Registered successfully"
                return redirect('login')
                
        except Exception as e:
            msg = f"Server Error: {e}"
    
    return render(request, "register.html", {"msg": msg})

def logout(request):
    auth_logout(request)
    return redirect('login')  

@login_required
def change_password(request):
    msg = ""
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        user = request.user

        # Validate old password
        if not user.check_password(old_password):
            msg = "Current password is incorrect."
        elif new_password != confirm_password:
            msg = "New passwords do not match."
        elif len(new_password) < 8:
            msg = "New password must be at least 8 characters long."
        elif not re.search(r"[A-Z]", new_password):
            msg = "New password must contain at least one uppercase letter."
        elif not re.search(r"[a-z]", new_password):
            msg = "New password must contain at least one lowercase letter."
        elif not re.search(r"[0-9]", new_password):
            msg = "New password must contain at least one digit."
        elif not re.search(r"[\W_]", new_password):
            msg = "New password must contain at least one special character."
        else:
            # Update password
            user.password = make_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # Keep the user logged in
            messages.success(request, "Your password was successfully updated!")
            return redirect('home')

    return render(request, 'change_password.html', {'msg': msg})

@login_required
def home(request):
    msg = ''
    return render(request, 'index.html', {'msg': msg})

@login_required
def about(request):
    msg = ''
    return render(request, 'about.html', {'msg': msg})

@login_required
def symptoms(request):
    msg = ''
    return render(request, 'symptoms.html', {'msg': msg})

@login_required
def prevention(request):
    msg = ''
    return render(request, 'prevention.html', {'msg': msg})

@login_required
def doctors(request):
    msg = ''
    return render(request, 'doctors.html', {'msg': msg})

@login_required
def predict(request):
    msg=""
    if request.method == "POST":
        age = float(request.POST.get("Age"))
        sex = float(request.POST.get("gender"))
        rbc = float(request.POST.get("rbccount"))
        pcv = float(request.POST.get("pcv"))
        mcv = float(request.POST.get("mcv"))
        mch = float(request.POST.get("mch"))
        mchc = float(request.POST.get("mchc"))
        rdw = float(request.POST.get("rdwc"))
        tlc = float(request.POST.get("tlc"))
        plt = float(request.POST.get("plt"))
        hgb = float(request.POST.get("hgb"))
        df = pd.read_csv(('static/anemiaPredictionDataset.csv'))
        print(df.to_string())
        # plt.figure()
        # df.hist()
        # scatter_matrix(df)
        # sns.scatterplot(df)
        # plt.show()
        # df.plot()
        # pyplot.show()

        log_regress_model = linear_model.LogisticRegression(max_iter=3000)
        # svm_model = svm.SVC(max_iter=3000)
        y = df.values[:, 11]
        X = df.values[:, 0:11]
        X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3)

        print(X)
        print(y)

        log_regress_model.fit(X_train, y_train)
        # svm_model.fit(X_train, y_train)

        print(log_regress_model.predict([[28, 0, 0, 34, 60, 17, 28, 20, 11, 0, 14]]))

        y_predict_log = log_regress_model.predict(X_test)
        print(metrics.accuracy_score(y_test, y_predict_log))

        if sex == 0 or sex == 1:
            print(log_regress_model.predict([[age, sex, rbc, pcv, mcv, mch, mchc, rdw, tlc, plt, hgb]]))
            result = log_regress_model.predict([[age, sex, rbc, pcv, mcv, mch, mchc, rdw, tlc, plt, hgb]])

            if result != 0:
                msg="Result: You are Anemic!Consult Doctor"
            else:
                msg="Result: Your are NOT ANEMIC"
        else:
            msg="Input Error", "Please enter 0 or 1 in the SEX field"
        print(msg)


    return render(request, 'predict.html',{"msg":msg})
