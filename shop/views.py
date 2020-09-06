from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    print(f"is user logged in : {request.user.is_authenticated}")
    context = {
        "title": "صفحه ی اصلی",
        "content": "به آموزش جنگو خوش آمدید"
    }

    if request.user.is_authenticated:
        context["new_content"] = "this is new content"

    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "درباره ما",
        "content": "ما برنامه نویسان جنگو در تاپ لرن هستیم"
    }

    return render(request, "about_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "تماس با ما",
        "content": "this is contact page",
        "form": contact_form
    }

    if contact_form.is_valid():
        result = contact_form.cleaned_data
        print(result)
        print(result["fullname"])

    # if request.method == "POST":
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('message'))

    return render(request, 'contact/view.html', context)


def login_page(request):
    print(f"is user logged in : {request.user.is_authenticated}")
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        userName = form.cleaned_data.get("userName")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            context["form"] = LoginForm()
            return redirect('/')
        else:
            print("Error")

    return render(request, "auth/login.html", context)


# get user model ( class )
User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        userName = form.cleaned_data.get("userName")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username=userName, email=email, password=password)
        print(new_user)

    return render(request, "auth/register.html", context)
