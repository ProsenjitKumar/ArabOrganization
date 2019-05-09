from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm
from django.contrib.auth import get_user_model
#from .models import User

User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    username = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)


# get data as choice field
def get_state():
    for user in User.objects.all():
        name = [
            (user.state, user.state)
        ]
    return name


def get_city():
    for user in User.objects.all():
        name = [
            (user.city, user.city)
        ]
    return name


def get_org_types():
    for user in User.objects.all():
        name = [
            (user.org_types, user.org_types)
        ]
    return name


def get_bank_name():
    for user in User.objects.all():
        name = [
            (user.bank_name, user.bank_name)
        ]
    return name


class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'org_name', 'org_short_name', 'logo', 'photo', 'address', 'telephone', 'whatsapp', 'fax', 'p_o_box',
                  'permit_number', 'permit_date', 'board_members', 'info', 'org_types', 'goals', 'projects',
                  'state', 'city', 'org_links')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = False # send for admin approval
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'org_name', 'org_short_name', 'logo', 'address', 'telephone', 'whatsapp',
                  'fax', 'p_o_box', 'permit_number', 'permit_date', 'board_members', 'info', 'org_types', 'goals',
                  'projects', 'state', 'city', 'org_links', 'bank_name', 'bank_account_name', 'bank_account_no',
                  'bank_account_short_info', 'position', 'photo')


# class BankInfoForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super(BankInfoForm, self).__init__(*args, **kwargs)
#     bank_name =  forms.CharField(label='Bank Name', widget=forms.Select(choices=get_bank_name()))
#     bank_account_name = forms.CharField(max_length=100)
#     bank_account_no = forms.CharField(max_length=100)
#     bank_account_short_info = forms.CharField(widget=forms.Textarea)
#     position = forms.IntegerField()
#     photo = forms.ImageField(required=False)
#
#
# class CrispyBankInfoForm(BankInfoForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Row(
#                 Field('bank_name', css_class='form-group col-md-6 mb-0'),
#                 Column('bank_account_name', css_class='form-group col-md-6 mb-0'),
#                 Column('bank_account_no', css_class='form-group col-md-6 mb-0'),
#                 Column('position', css_class='form-group col-md-6 mb-0'),
#                 Column('photo', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
#             Row(
#                 Column('bank_account_short_info', css_class='form-group col-md-6 mb-0'),
#             ),
#             Submit('submit', 'Submit')
#         )


class BankInfoForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('bank_name', 'bank_account_name', 'bank_account_no',
                  'bank_account_short_info', 'position', 'photo',)
        # labels = {
        #     'bank_name': _('name Of the Bank'),
        # }
        # help_texts = {
        #     'bank_account_no': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'bank_account_short_info': {
        #         'max_length': _("This Info is too long."),
        #     },
        # }






















