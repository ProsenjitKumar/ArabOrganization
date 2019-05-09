import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.urls import reverse


# ------------------------------------------------------------------------
# -------- Organization type as drop list or category
class OrgType(models.Model):
    name = models.CharField(max_length=66)
    slug = models.SlugField()

    # Auto create slug according to Organization Type name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(OrgType, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# -------- State type as drop list or category
class State(models.Model):
    name = models.CharField(max_length=66)
    slug = models.SlugField()

    # Auto create slug according to state name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(State, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# -------- City type as drop list or category
class City(models.Model):
    name = models.CharField(max_length=66)
    slug = models.SlugField()

    # Auto create slug according to city name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# -------- Bank Name type as drop list or category
class Bank(models.Model):
    name = models.CharField(max_length=66)
    slug = models.SlugField()

    # Auto create slug according to Bank name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Bank, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# ------------------ Base user manager ------------------
class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an Email address.")
        if not password:
            raise ValueError("Users must have a Password")
        if not full_name:
            raise ValueError("Users must have a Full Name")
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name=full_name
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True,
            is_admin=False # will be True
        )
        return user


# -------- Organization All User Field
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True) # Can Login
    staff = models.BooleanField(default=False) # staff user non Superuser
    admin = models.BooleanField(default=False) # Superuser
    timestamp = models.DateTimeField(auto_now_add=True)

    # Profile
    org_name = models.CharField(max_length=200)
    org_short_name = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to='org_logo/', blank=True)
    address = models.CharField(max_length=260)
    telephone = models.IntegerField(blank=True, null=True)
    whatsapp = models.IntegerField(blank=True, null=True)
    fax = models.CharField(max_length=50)
    p_o_box = models.CharField(max_length=80)
    permit_number = models.CharField(max_length=15, null=True)
    permit_date = models.CharField(max_length=10, null=True)
    board_members = models.TextField()
    info = models.TextField()
    org_types = models.ForeignKey(OrgType, on_delete=models.CASCADE, null=True)
    goals = models.TextField()
    projects = models.TextField()
    # permit Issuer
    permit = models.BooleanField(default=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    org_links = models.URLField(blank=True)
    bank_name = models.ForeignKey(Bank, on_delete=models.CASCADE, blank=True, null=True)
    bank_account_name = models.CharField(max_length=100, blank=True, null=True)
    bank_account_no = models.CharField(max_length=100, unique=True, null=True, blank=True)
    bank_account_short_info = models.TextField(blank=True, null=True)
    position = models.PositiveSmallIntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_photo/', blank=True, null=True)
    # Created at, updated at by(user name), ip, mac, address
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    USERNAME_FIELD = 'email'  # Username
    # USERNAME_FILED and password are required by default
    REQUIRED_FIELDS = ['full_name'] # 'full_name'

    objects = UserManager()

    class Meta:
        ordering = ('org_name',)
        index_together = (('id', 'slug'),)

    # Auto create slug according to Organization name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.org_name)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.org_name

    def get_absolute_url(self):
        return reverse('single_organization_detail', args=[self.id, self.slug])

    def  get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)





