from django.shortcuts import render,HttpResponse
from.models import Course
# Create your views here.
def home(request):
    return render(request,'home.html')

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
                return redirect("register")
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
                details.gender = request.POST["radio"]
                details.date = request.POST["date"]
                details.city = request.POST["city"]
                details.state = request.POST["state"]
                details.country = request.POST["country"]
                details.pincode = request.POST["pincode"]
                details.upload_image = request.FILES["file"]
                details.save()
                return redirect("login")
        else:
            return redirect("register")
    else:
    return render(request,'registration.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)

            if user.check_password(password):
                auth.login(request, user)
                return redirect("dashboard")
            else:
                return render(request, "login.html")
        else:
            return render(request, "login.html")
    else:
        return render(request, "login.html")
def course(request):
    details=Course.objects.all()
    return render(request,'course.html',{"Course":details})
def dashboard(request):
    user = request.user
    user_data = User.objects.get(id=user.id)
    print(user_data)
    print(user.id)
    profile_data = Profile.objects.get(user_id=user.id)
    return render(request, "dashboard.html", {"userDetails": user_data, "profileData": profile_data})
