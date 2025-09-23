#This file holds Workerfy's form models

from .models import WorkerfyUser, Client, Tradesperson
from django import forms
from django.contrib.auth.forms import UserCreationForm


# This is a login form
class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'id': 'email',
            'placeholder': 'Email or Username',
            'required': True,
            'autofocus': True,
        })
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'placeholder': 'Password',
            'required': True,
        })
    )

# This form is used to create a new User
class WorkerfyUserForm(UserCreationForm):
    #password = forms.CharField(widget=forms.PasswordInput, required=True, label="Password")
    password1 = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={'id':'password', 'placeholder': 'Enter Password', 'required': True}))
    password2 = forms.CharField(label="Password Confirm", strip=False, widget=forms.PasswordInput(attrs={'id':'password', 'placeholder': 'Confirm Password', 'required': True}))    
    class Meta:
        model = WorkerfyUser
        fields = ['email', 'password1', 'password2']  # Define only the fields to display
        widgets = {
            'email': forms.EmailInput(attrs={'id': 'S_email', 'autofocus': False, 'placeholder': 'Enter your email', 'required': True, 'autocomplete': 'off'}),
            'password1': forms.PasswordInput(attrs={'id': 'S_password'}),
            'password2': forms.PasswordInput(attrs={'id': 'S_password2'}),
        }
        labels = {
            'email': 'Email:',
            'password1': 'Password:',
            'password2': 'Password Confirm:',
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'middle_name', 'last_name', 'profile_picture', 'phone', 'phone2', 'location', 'address', 'bio']
        widgets = {
            'first_name': forms.TextInput(attrs={'id': 'CT_firstname', 'autofocus': True}),
            'middle_name': forms.TextInput(attrs={'id': 'CT_othernames'}),
            'last_name': forms.TextInput(attrs={'id': 'CT_lastname', 'required': True}),
            'profile_picture': forms.FileInput(attrs={'id': 'CT_profilePicture'}),
            'phone': forms.TextInput(attrs={'id': 'CTphone1', 'required': True, 'pattern': '[0-9]{10}'}),
            'phone2': forms.TextInput(attrs={'id': 'CTphone2', 'pattern': '[0-9]{10}'}),
            'location': forms.Select(attrs={'id': 'CT_location'}, choices=[
                ('Greater Accra', 'Greater Accra'), ('Volta', 'Volta Region'),
                ('Ashanti', 'Ashanti Region'), ('Western_North', 'Western North Region'),
                ('Western', 'Western Region'), ('Central', 'Central Region'),
                ('Upper_East', 'Upper East Region'), ('Savannah', 'Savannah Region'),
                ('North_East', 'North East Region'), ('Bono', 'Bono Region'),
                ('Ahafo', 'Ahafo Region'), ('Bono_East', 'Bono East Region'),
                ('Upper_West', 'Upper West Region'), ('Nortern', 'Nortern Region'),
                ('Oti', 'Oti Region'), ('Eastern', 'Eastern Region')
            ]),
            'address': forms.TextInput(attrs={'id': 'CT_address'}),
            'bio': forms.Textarea(attrs={'id': 'CT_Bio', 'placeholder': 'Tell who you are', 'rows': 4, 'cols': 60, 'style': 'height: 100px;'}),
        }
        labels = {
            'first_name': 'First Name:',
            'middle_name': 'Other Names:',
            'last_name': 'Last Name:',
            'profile_picture': 'Profile Picture:',
            'phone': 'Phone Number:',
            'phone2': 'Second Phone Number:',
            'location': 'Region you are based:',
            'address': 'The area you work in in your region:',
            'bio': 'The area you work in in your region:'
        }

# This form handles the registration of Tradespeople
class TradespersonForm(forms.ModelForm):
    class Meta:
        model = Tradesperson
        fields = [
            'first_name', 'middle_name', 'last_name', 'profile_picture', 
            'phone', 'phone2', 'location', 'address', 'trades_type', 'specialization', 'years_of_experience', 'extra_skills', 'certification', 
            'work_hours', 'job_type', 'service_range', 'rate_charged', 'languages', 'availability_status', 'bio'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'id': 'CT_firstname', 'autofocus': True, 'required': True}),
            'middle_name': forms.TextInput(attrs={'id': 'CT_othernames'}),
            'last_name': forms.TextInput(attrs={'id': 'CT_lastname', 'required': True}),
            'profile_picture': forms.FileInput(attrs={'id': 'CT_profilePicture', 'required': True}),
            'phone': forms.TextInput(attrs={'id': 'CTphone1', 'required': True, 'pattern': '[0-9]{3}-[0-9]{3}-[0-9]{4}'}),
            'phone2': forms.TextInput(attrs={'id': 'CTphone2', 'pattern': '[0-9]{3}-[0-9]{3}-[0-9]{4}'}),
            'location': forms.Select(attrs={'id': 'CT_location', 'required': True}),
            'address': forms.TextInput(attrs={'id': 'CT_address'}),
            'trades_type': forms.Select(attrs={'id': 'CT_specialization'}),
            'specialization': forms.TextInput(attrs={'id': 'CT_address'}),
            'years_of_experience': forms.NumberInput(attrs={'id': 'CT_experience', 'min': '1'}),
            'extra_skills': forms.Select(attrs={'id': 'CT_tradestype'}),
            'certification': forms.TextInput(attrs={'id': 'CT_certification'}),
            'work_hours': forms.TimeInput(attrs={'id': 'CT_workHoursStart'}),
            'job_type': forms.Select(attrs={'id': 'CT_jobType'}),
            'service_range': forms.Select(attrs={'id': 'CT_serviceRange'}),
            'rate_charged': forms.NumberInput(attrs={'id': 'CT_Rate'}),
            'language': forms.TextInput(attrs={'id': 'CT_language'}),
            'availability_status': forms.Select(attrs={'id': 'CT_availability', 'required': True}),
            'bio': forms.Textarea(attrs={'id': 'CT_Bio', 'rows': 20, 'cols': 50, 'placeholder': 'Tell who you are'}),
        }
        labels = {
            'first_name': 'First Name:',
            'middle_name': 'Other Names:',
            'last_name': 'Last Name:',
            'profile_picture': 'Profile Picture:', 
            'phone': 'Phone Number:',
            'phone2': 'Second Phone Number:',
            'location': 'Region you are based:',
            'address': 'The area you work in in your region:',
            'trades_type': 'What kind of trades work do you do:', 
            'specialization': 'What do you specialize in your field:',
            'years_of_experience': 'How many years of experience do you have:',
            'extra_skills': 'Do you have any extra skill in you field. State it here:',
            'certification': 'Do hold any certificate. List your latest or most valuable certificate:', 
            'work_hours': 'What time do you start work:',
            'job_type': 'What is you job type(Part time, Full time, Freelance contracts):',
            'service_range': 'What is your job range:', 
            'past_jobs': 'Upload pictures of your past Work. This will be verfied. Use you own pictures(Max:10 pictures):',
            'rate_charged': 'What is you rate per Job(in GHc):',
            'language': 'What languages are you fluent(Separeate with a (,)):',
            'availability_status': 'What is you Availability status:',
            'bio': 'Write about yourself.(Tell Clients why you are the best fit.):',

        }

# This is a form for the verification by email page
class verificationByEmailForm(forms.Form):
    code = forms.UUIDField(label='Verification Code')


    

