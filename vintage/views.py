from django.conf import settings
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from.models import Course,Profile
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def profile(request):
    return render(request,'profile.html')
def registration(request):
    if request.method == "POST":
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists() or \
                    User.objects.filter(email=email).exists():
                return redirect("registration")
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=firstname,
                    last_name=lastname
                )
                subject = "Welcome to Vintage Info Solutions"
                message = f"Hai {user.first_name, user.last_name}, Thank you for registering in Vintage Info Solutions"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail(subject, message, email_from, recipient_list)
                details = Profile()
                details.user = user
                details.gender = request.POST["gender"]
                details.dateofbirth = request.POST["dateofbirth"]
                details.save()
                return redirect("login")
        else:
            return redirect("registration")
    else:
        return render(request,'registration.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")

        user = auth.authenticate(request,username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")  # Redirect to a success page after login
        else:
            messages.error(request, "Bad credentials")
            return render(request, "login.html")  # Show the login page with an error message

    return render(request, "login.html")
def course(request):
    details=Course.objects.all()
    return render(request,'course.html',{"Course":details})
# def dashboard(request):
#     user = request.user
#     user_data = User.objects.get(id=user.id)
#     print(user_data)
#     print(user.id)
#     profile_data = Profile.objects.get(user_id=user.id)
#     return render(request, "dashboard.html", {"userDetails": user_data, "profileData": profile_data})



# @login_required
# def dashboard(request):
#     user = request.user
#
#     try:
#         # Assuming User is the default User model, no need to use get_object_or_404 here
#         user_data = User.objects.get(id=user.id)
#         profile_data = Profile.objects.get(user=user_data)
#     except User.DoesNotExist:
#         user_data = None
#     except Profile.DoesNotExist:
#         profile_data = None
#
#     full_name = user_data.get_full_name() if user_data else None
#
#     return render(request, "dashboard.html", {"userDetails": user_data, "profileData": profile_data, "fullName": full_name})

@login_required
def dashboard(request):
    user = request.user
    try:
        profile_data = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile_data = None
        # Log the error or print a message for debugging
        print("Profile not found for user:", user)

    context = {
        'userDetails': user,
        'profileData': profile_data,
    }
    return render(request, 'dashboard.html', context)
def logout(request):
    auth.logout(request)
    request.session["user_status"]="logged out"
    return redirect("home")