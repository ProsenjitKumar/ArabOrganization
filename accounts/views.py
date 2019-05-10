from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .forms import RegisterForm, LoginForm, BankInfoForm
from django.db.models import Q
from .models import BankInfo
from django.views.generic import FormView, TemplateView


# Home View
def home(request):
    users = User.objects.filter(permit=True)
    banks = BankInfo.objects.all()
    #banks = BankInfo.objects.all().order_by('created_at')[:2:1]
    context = {"users": users, "banks": banks}
    return render(request, 'home.html', context)


def single_organization_detail(request, id, slug):
    # user = User.objects.get(pk=user_id)
    user = get_object_or_404(User, id=id, slug=slug)
    context = {"user": user}
    return render(request, 'organizer/single-organization-detail.html', context)


# all bank account
def all_bank_account(request):
    banks = BankInfo.objects.all()
    user = request.user
    context = {
        'banks': banks,
        'user': user
    }
    return render(request, 'profile/all-bank-account.html', context)


def single_bank_account_detail(request, id, slug):
    # user = User.objects.get(pk=user_id)
    user = get_object_or_404(BankInfo, id=id, slug=slug)
    context = {"bank": user}
    return render(request, 'profile/single-bank-account.html', context)


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
    form = RegisterForm(request.POST or None, request.FILES)
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
    user = request.user
    #form = BankInfoForm(request.POST)
    #form = BankInfoForm()
    if request.method == 'POST':
        form = BankInfoForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return render(request, 'profile/success-bank-info-add-update.html')
    else:
        form = BankInfoForm(instance=request.user)
        context = {
            "banks": BankInfo.objects.filter(user=user),
            "form": form,
        }
        return render(request, 'profile/bank-info-add-update.html', context)

# class BankInfoFormView(FormView):
#     template_name = 'profile/bank-info-add-update.html'
#     form_class = BankInfoForm
#     success_url = '/success/'
#
#     # def get_context_data(self, **kwargs):
#     #     context = super(BankInfoFormView, self).get_context_data(**kwargs)
#     #     #context["testing_out"] = "this is a new context var"
#     #     return context
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.save()
#         return super(BankInfoFormView, self).form_valid(form)


class Success(TemplateView):
    template_name = "profile/success-bank-info-add-update.html"

# ***************************
def available_organizer(request):
    if request.method == 'POST':
        search = request.POST['search']

        if search:
            match = User.objects.filter(
                Q(full_name__startswith=search) |
                Q(email__icontains=search)
            )
            if match:
                return render(request, 'organizer/available-organization.html', {"match": match})
            else:
                messages.error(request, "No result found")

        if search:
            match = BankInfo.objects.filter(
                Q(bank_account_name__contains=search) |
                Q(bank_account_no__contains=search)

            )
            if match:
                return render(request, 'organizer/available-organization.html', {"match": match})
            else:
                messages.error(request, "No result found")
        else:
            return HttpResponseRedirect('/')

    args = {
        "users": User.objects.filter(permit=True),
    }
    return render(request, 'index.html', args)








