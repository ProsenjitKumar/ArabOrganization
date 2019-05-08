from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import RegisterForm, LoginForm, BankInfoForm
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError


# Home View
def home(request):
    users = User.objects.filter(permit=True)
    context = {"users": users}
    return render(request, 'index.html', context)


def single_organization_detail(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {"user": user}
    return render(request, 'organizer/single-organization-detail.html', context)


# Login Page
@csrf_protect
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        #user.active = False
        if user is not None:
            # Is the account active? It could have been disabled.
            # user.is_active = False
            if user.is_active:
                login(request, user)
                # return render(request, 'profile/index.html')
                return HttpResponseRedirect("/profile/") #or you may use
            else:
                return HttpResponse("You have to Wait for admin approval.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'accounts/pass_admin_approval_wrong.html')
    else:
        return render(request, 'accounts/login.html', context)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')


# Register Page
User = get_user_model()
@csrf_protect
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        return render(request, 'accounts/register_success.html')
    return render(request, 'accounts/register.html', context)


# User Profile Page
@login_required
def profile(request):
    args = {"user": request.user}

    return render(request, 'profile/profile.html', args)


# Bank Info Add and update
@login_required
def bank_info_add_update(request):
    if request.method == 'POST':
        form = BankInfoForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'profile/success-bank-info-add-update.html')
    else:
        form = BankInfoForm(instance=request.user)
        context = {
            "form": form,
        }
        return render(request, 'profile/bank-info-add-update.html', context)


def available_organizer(request):
    if request.method == 'POST':
        search = request.POST['search']

        if search:
            match = User.objects.filter(
                Q(full_name__startswith=search) |
                Q(email__icontains=search) |
                Q(bank_account_name__startswith=search) |
                Q(position__icontains=search)
            )
            if match:
                return render(request, 'organizer/available-organization.html', {"match": match})
            else:
                messages.error(request, "No result found")
        else:
            return HttpResponseRedirect('/')

    args = {
        "users": User.objects.all(),
    }
    return render(request, 'index.html', args)








