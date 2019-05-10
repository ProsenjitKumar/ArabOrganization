from django.contrib import admin
from .models import Bank, State, City, OrgType,\
    User, BankInfo, OrgLinks


# Organization field show in admin panel
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['org_name', 'org_short_name', 'telephone',
                    'permit', 'active', 'slug', 'state', 'city']
    exclude = ('password', 'last_login', 'staff', 'admin', 'full_name',)
    list_per_page = 20
    search_fields = ['org_name', 'org_short_name', 'telephone',
                    'state', 'city']
    prepopulated_fields = {'slug': ('org_name',)}


admin.site.register(User, OrganizationAdmin)


# bank Info
class BankInfoAdmin(admin.ModelAdmin):
    list_display = ['bank_name', 'permit',
                    'bank_account_name', 'position']
    list_per_page = 20
    search_fields = ['org_name', 'org_short_name', 'telephone',
                    'state', 'city', 'bank_name',
                    'bank_account_name', 'position']
    prepopulated_fields = {'slug': ('bank_name',)}


admin.site.register(BankInfo, BankInfoAdmin)


# Organization field show in admin panel
class BankAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 20
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Bank, BankAdmin)


# Organization field show in admin panel
class StateAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 20
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(State, StateAdmin)


# Organization field show in admin panel
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 20
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(City, CityAdmin)


# Organization field show in admin panel
class OrgTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 20
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(OrgType, OrgTypeAdmin)

'''
# Organization Org Links field show in admin panel
class OrgLinksAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 20
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(OrgLinks, OrgLinksAdmin)
'''






