from django.contrib import admin
from django.contrib import admin
from Registration.models import Registration

# Register your models here.

class Registration_User(admin.ModelAdmin):
    list_RegistrationUser = (
        ' registar_Fname,'
 'registar_Email',
' registar_Mobile',
 'registar_Dob',
 'registar_Password',
 'registar_ConfmPassword'
    )

admin.site.register(Registration, Registration_User)
