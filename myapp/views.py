from django.shortcuts import render, redirect
from django.contrib import messages
from pymongo import MongoClient
from bson.objectid import ObjectId
import hashlib
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password

client = MongoClient("mongodb://localhost:27017/")
db = client.corelink
students_collection = db.students

from pymongo.errors import ConnectionFailure

try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
    client.admin.command('ping')  # Pings the MongoDB server
    print("✅ MongoDB connection successful!")
except ConnectionFailure as e:
    print("❌ MongoDB connection failed:", e)

def home(request):
    return render(request, 'myapp/dashboard.html')

def index(request):
    return render(request, 'myapp/index.html')
    
def nlp(request):
    return render(request, 'myapp/nlp.html')

def probability(request):
    return render(request, 'myapp/nlp_prob.html')

def python(request):
    return render(request, 'myapp/nlp_python.html')

def regular(request):
    return render(request, 'myapp/regular.html')

def tokenization(request):
    return render(request, 'myapp/tokenization.html')

def object(request):
    return render(request, 'myapp/object.html')

def oops(request):
    return render(request, 'myapp/oops.html')

# def profile(request):
#     return render(request, 'myapp/profile.html')

def register_student(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        branch = request.POST['branch']

        if branch not in ["ARI", "CSE"]:  # Extra validation for security
            return render(request, 'register.html', {"error": "Invalid branch selected"})

        student = Student(name=name, email=email, password=password, branch=branch)
        student.save()
        return redirect('success')  # Redirect after registration

    return render(request, 'register.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Student  # Make sure this matches your custom user model

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         user = authenticate(request, email=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             messages.success(request, f"Welcome {user.name}!")
#             # Redirect based on role (optional)
#             if user.role == 'admin':
#                 return redirect('admin_dashboard')
#             else:
#                 return redirect('student_dashboard')
#         else:
#             messages.error(request, "Invalid email or password.")
    
    #return render(request, 'myapp/dashboard.html')  # Replace with your login template



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('myapp/dashboard')  # ✅ Make sure 'dashboard' is a valid URL name
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "myapp/index.html")


from django.shortcuts import render

def dashboard_view(request):
    # your logic here
    return render(request, 'myapp/dashboard.html')  


def student_dashboard(request):
    return render(request, 'myapp/dashboard.html')  # Your student's dashboard template

def admin_dashboard(request):
    return render(request, 'myapp/admin_dashboard.html')  # Your admin's dashboard template

def oops_html(request):
    return render(request, 'myapp/class_objects_mthods.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def student_dashboard(request):
    user = request.user
    student_name = user.first_name.strip().upper() if user.first_name else user.username
    return render(request, 'myapp/dashboard.html', {'student_name': student_name})

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2')

def profile(request):
    user = request.user
    first_name = user.first_name.strip() if user.first_name else user.username
    last_name = user.last_name.strip() if user.last_name else user.username
    email = user.email.strip() if user.email else user.username
    return render(request, 'myapp/profile.html', {'first_name': first_name,'last_name': last_name,'email': email })


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')