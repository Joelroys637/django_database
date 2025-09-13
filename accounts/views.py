from django.shortcuts import render, redirect
from django.contrib import messages
from database.firebase_config import db

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Firebase Database reference
        ref = db.reference("users")

        # Check if user already exists
        existing_user = ref.order_by_child("email").equal_to(email).get()
        if existing_user:
            messages.error(request, "Email already registered!")
            return redirect("register")

        # Save new user
        user_data = {
            "username": username,
            "email": email,
            "password": password  # ⚠️ For demo only, use hashing in real apps
        }
        ref.push(user_data)

        messages.success(request, "Registration successful!")
        return redirect("register")

    return render(request, "accounts/register.html")
