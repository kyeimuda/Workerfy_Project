from django import forms
from .models import TradeCategory, TradeSpecialty, TradespersonProfile, Region, City, Country

class TradespersonOnboardingForm(forms.ModelForm):

    '''trade_specialties = forms.CharField(
        widget=forms.TextInput(attrs={'list': 'specialties-list', 'placeholder': 'e.g. Ceiling Fan Repair'}),
        required=False
    )
    skills = forms.CharField(
        widget=forms.TextInput(attrs={'list': 'skills-list', 'placeholder': 'e.g. Wiring'}),
        required=False
    )
    sub_location = forms.CharField(
        widget=forms.TextInput(attrs={'list': 'cities-list', 'placeholder': 'e.g. Madina'}),
        required=False
    )
    work_areas = forms.CharField(
        widget=forms.TextInput(attrs={'list': 'areas-list', 'placeholder': 'e.g. Accra New Town'}),
        required=False
    )
'''
    class Meta:
        model = TradespersonProfile
        fields = [
            "first_name",
            "last_name",
            "other_names",
            "profile_picture",
            "bio",
            "contact_number",
            "contact_number2",
            "date_of_birth",
            "gender",
            "trade_category",
            "trade_specialties",
            "skills",
            "base_location",
            "sub_location",
            "work_areas",
            "social_links",
            "working_areas"
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={'type': 'text', 'id': 'FName', 'placeholder': 'Kofi', 'required': True}),
            "last_name": forms.TextInput(attrs={'type': 'text', 'id': 'LName', 'placeholder': 'Dan', 'required': True}),
            "other_names": forms.TextInput(attrs={'type': 'text', 'id': 'Other', 'placeholder': 'Kyeimuda'}),
            "profile_picture": forms.FileInput(attrs={'id': 'ProfilePicture'}),
            "contact_number": forms.TextInput(attrs={'type': 'tel', 'id': 'Phone', 'placeholder': '050 524 1706', 'required': True}),
            "contact_number2": forms.TextInput(attrs={'type': 'tel', 'id': 'OtherPhone', 'placeholder': '050 300 4659'}),
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "bio": forms.Textarea(attrs={"rows": 3}),
            #"trade_specialties": forms.CheckboxSelectMultiple(),
            #"skills": forms.CheckboxSelectMultiple(),
            #"work_areas": forms.CheckboxSelectMultiple(),
        }


class TradespersonOnboardingForm2(forms.Form):
    # Basic Info
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(attrs={
            "type": "text",
            "id": "FName",
            "placeholder": "Kofi",
            "required": True,
            "class": "form-control"
        })
    )
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(attrs={
            "type": "text",
            "id": "LName",
            "placeholder": "Dan",
            "required": True,
            "class": "form-control"
        })
    )
    other_names = forms.CharField(
        label="Other Names",
        required=False,
        widget=forms.TextInput(attrs={
            "type": "text",
            "id": "Other",
            "placeholder": "Kyeimuda",
            "class": "form-control"
        })
    )

    # Contact Info
    contact_number = forms.CharField(
        label="Primary Contact",
        widget=forms.TextInput(attrs={
            "type": "tel",
            "id": "Phone",
            "placeholder": "050 524 1706",
            "required": True,
            "class": "form-control"
        })
    )
    contact_number2 = forms.CharField(
        label="Other Contact",
        required=False,
        widget=forms.TextInput(attrs={
            "type": "tel",
            "id": "OtherPhone",
            "placeholder": "050 300 4659",
            "class": "form-control"
        })
    )

    # Professional Info
    trade_category = forms.ModelChoiceField(
        label="Trade Category",
        queryset=TradeCategory.objects.all(),
        empty_label="Select Trade Category eg.Electrician",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    
    trade_specialties = forms.CharField(
        label="Specialties",
        required=False,
        widget=forms.TextInput(attrs={
            "type": "text",
            "placeholder": "e.g. Ceiling Fan Repair",
            "class": "form-control"
        })
    )
    skills = forms.CharField(
        label="Skills",
        required=False,
        widget=forms.TextInput(attrs={
            "type": "text",
            "placeholder": "e.g. Wiring",
            "class": "form-control"
        })
    )

    # Location Info
    country = forms.ModelChoiceField(
        label="Country",
        queryset=Country.objects.all(),
        empty_label="Select Country",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    base_location = forms.ModelChoiceField(
        label="Region",
        queryset=Region.objects.all(),
        empty_label="Select Region",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    
    sub_location = forms.ModelChoiceField(
        label="City / Town",
        queryset=City.objects.all(),
        empty_label="Select City",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    work_areas = forms.CharField(
        label="Work Areas",
        required=False,
        widget=forms.TextInput(attrs={
            "type": "text",
            "placeholder": "e.g. Accra New Town",
            "class": "form-control"
        })
    )

    # Extras
    profile_picture = forms.FileField(
        label="Profile Picture",
        required=False,
        widget=forms.FileInput(attrs={
            "id": "ProfilePicture",
            "class": "form-control"
        })
    )
    date_of_birth = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control"
        })
    )
    gender = forms.ChoiceField(
        label="Gender",
        choices=[("male", "Male"), ("female", "Female"), ("other", "Other")],
        widget=forms.Select(attrs={
            "class": "form-control"
        })
    )
    bio = forms.CharField(
        label="About You",
        required=False,
        widget=forms.Textarea(attrs={
            "rows": 3,
            "placeholder": "Write about yourself........ ",
            "class": "form-control"
        })
    )
    social_links = forms.URLField(
        label="Social Media Link",
        required=False,
        widget=forms.URLInput(attrs={
            "placeholder": "https://facebook.com/yourprofile",
            "class": "form-control"
        })
    )

class ProfileEditPageform(forms.Form):
    first_name = forms.CharField(
        max_length=150,
        required=False,
        label="First Name",
        widget=forms.TextInput(attrs={
            "type": "text",
            "id": "First_Name",
            "placeholder": 'kofi',
            "class": "inputField"
        })
    )

    last_name = forms.CharField(
        max_length=150,
        label="Last Name",
        required=False,
        widget=forms.TextInput(attrs={
            "type": "text",
            "id": "Last_Name",
            "placeholder": "Dan",
            "class": "inputField"
        })
    )

    other_names = forms.CharField(
        max_length=150,
        label="Other Names",
        required=False,
        widget=forms.TextInput(attrs={
            "type": "text",
            "id": "Other",
            "placeholder": "Kyeimuda",
            "class": "inputField"
        })
    )

    username = forms.CharField(
        max_length=150, 
        required=False, 
        widget=forms.TextInput(attrs={
            "type": "text",
            "id": "Other",
            "placeholder": "Kyeimuda",
            "class": "inputField"
        })
    )
    
    profile_picture = forms.ImageField(
        label="Profile Picture",
        required=False,
        widget=forms.FileInput(attrs={
            "id": "ProfilePicture",
            "class": "inputField"
        })
    )
    

    bio = forms.CharField(
        label="Bio",
        required=False,
        widget=forms.Textarea(attrs={
            "rows": 3,
            "placeholder": "Write about yourself........ ",
            "class": "inputField"
        })
    )
    
    contact_number = forms.CharField(
        max_length=15,
        required=False,
        label="Primary Contact",
        widget=forms.TextInput(attrs={
            "type": "tel",
            "id": "Phone",
            "placeholder": "050 524 1706",
            "class": "inputField"
        })
    )

    contact_number2 = forms.CharField(
        label="Other Contact",
        required=False,
        widget=forms.TextInput(attrs={
            "type": "tel",
            "id": "OtherPhone",
            "placeholder": "050 300 4659",
            "class": "inputField"
        })
    )

    gender = forms.ChoiceField(
        choices = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        required=False,
        label= "Gender",
        widget=forms.Select(attrs={
            "id": "Gender",
            "class": "inputField"
        })
    )

    website = forms.URLField(
        required=False,
        label = "Website",
        widget = forms.URLInput(attrs={
            "type": "url",
            "id": "Website",
            "placeholder": "https://yourwebsite.com",
            "class": "inputField"
        })
    )

    date_of_birth = forms.DateField(
        label="Date of Birth",
        required=False,
        widget=forms.DateInput(attrs={
            "id": "Date_of_birth",
            "type": "date",
            "class": "inputField"
        })
    )

    experience_years = forms.IntegerField(
        min_value=0,
        required=False,
        widget=forms.NumberInput(attrs={
            "id": "Experience_Years",
            "class": "inputField",
            "placeholder": "Years of experience"
        })
    )

    trade_category = forms.ModelChoiceField(
        required=False,
        label="Trade Category",
        queryset=TradeCategory.objects.all(),
        empty_label="Select Trade Category eg.Electrician",
        widget=forms.Select(attrs={
            "id": "Trade_Category",
            "class": "inputField"
            })
    )

    trade_specialties = forms.CharField(
        label="Specialties",
        required=False,
        widget=forms.TextInput(attrs={
            "id": "Trade_Specialties",
            "placeholder": "e.g. Ceiling Fan Repair",
            "class": "inputField"
        })
    )
    skills = forms.CharField(
        label="Skills",
        required=False,
        widget=forms.TextInput(attrs={
            "id": "Skills",
            "placeholder": "e.g. Wiring",
            "class": "inputField"
        })
    )

    other_skills = forms.CharField(
        label="Other Skills",
        required=False,
        widget=forms.TextInput(attrs={
            "id": "OtherSkills",
            "placeholder": "e.g. Microsoft Word",
            "class": "inputField"
        })
    )

    country = forms.ModelChoiceField(
        required=False,
        label="Country",
        queryset=Country.objects.all(),
        empty_label="Select Country",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    base_location = forms.ModelChoiceField(
        required=False,
        label="Region",
        queryset=Region.objects.all(),
        empty_label="Select Region",
        widget=forms.Select(attrs={
            "id": "Base_Location",
            "class": "inputField",
            "placeholder": "e.g. Greater Accra",
            })
    )

    sub_location = forms.ModelChoiceField(
        required=False,
        label="City / Town",
        queryset=City.objects.all(),
        empty_label="Select City",
        widget=forms.Select(attrs={
            "id": "Sub_Location",
            "placeholder": "e.g. Accra",
            "class": "inputField"
            })
    )
    
    work_areas = forms.CharField(
        label="Work Area",
        required=False,
        widget=forms.TextInput(attrs={
            "type": "text",
            "placeholder": "e.g. Accra New Town",
            "class": "form-control"
        })
    )
    social_links = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "id": "Social_Links",
            "placeholder": "https://facebook.com/yourprofile",
            "class": "inputField"
        })
    )
    working_areas = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "id": "Working_Areas",
            "placeholder": "e.g. Accra, Tema",
            "class": "inputField"
        })
    )
    education_schools = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "id": "Education_Schools",
            "placeholder": "e.g. KNUST",
            "class": "inputField"
        })
    )

    availability_status = forms.ChoiceField(
        choices=[
            ("Available", "Available"),
            ("Urgent", "Urgent"),
            ("Busy", "Busy"),
            ("On Leave", "On Leave")
        ],
        initial="Available",
        required=False,
        widget=forms.Select(attrs={
            "id": "Availability_Status",
            "class": "inputField"
        })
    )

    other_skills = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "id": "education",
            "placeholder": "https://facebook.com/yourprofile",
            "class": "inputField"
        })
    )

class CertificateForm(forms.Form):
    title = forms.CharField(
        label="Certificate Title",
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={
            "placeholder": "e.g. Electrical Safety Certificate",
            "class": "form-control"
        })
    )
    description = forms.CharField(
        label="Description",
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "Brief description of the certificate",
            "class": "form-control",
            "rows": 3
        })
    )
    issuing_organization = forms.CharField(
        label="Issuing Organization",
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={
            "placeholder": "e.g. Ghana Electrical Board",
            "class": "form-control"
        })
    )
    issue_date = forms.DateField(
        label="Issue Date",
        required=False,
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control"
        })
    )
    expiry_date = forms.DateField(
        label="Expiry Date",
        required=False,
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control"
        })
    )
    certificate_file = forms.FileField(
        label="Certificate File",
        required=False,
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control"
        })
    )
    contact_person = forms.CharField(
        label="Contact Person",
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Person to contact for verification",
            "class": "form-control"
        })
    )
    contact_email = forms.EmailField(
        label="Contact Email",
        required=False,
        widget=forms.EmailInput(attrs={
            "placeholder": "Contact email for verification",
            "class": "form-control"
        })
    )
    contact_phone = forms.CharField(
        label="Contact Phone",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Contact phone for verification",
            "class": "form-control"
        })
    )
    verification_notes = forms.CharField(
        label="Verification Notes",
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "Additional instructions or context",
            "class": "form-control",
            "rows": 2
        })
    )

class PortfolioForm(forms.Form):
    titlePort = forms.CharField(
        label="Title",
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={
            "placeholder": "e.g. Kitchen Cabinet Installation",
            "class": "form-control"
        })
    )
    descriptionPort = forms.CharField(
        label="Description",
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "Describe this project...",
            "class": "form-control",
            "rows": 3
        })
    )
    image = forms.ImageField(
        label="Image",
        required=False,
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control"
        })
    )
    video = forms.FileField(
        label="Video",
        required=False,
        widget=forms.ClearableFileInput(attrs={
            "class": "form-control"
        })
    )