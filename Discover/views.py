from django.shortcuts import render, redirect
from .forms import LoginForm, WorkerfyUserForm, ClientForm, TradespersonForm, verificationByEmailForm
from django.contrib.auth import login, authenticate, logout
from MainWorkerfy.forms import TradespersonOnboardingForm, TradespersonOnboardingForm2
from MainWorkerfy.models import TradespersonProfile, City, Area, TradeSpecialty, TradeSkillTag, Region
from .models import WorkerfyUser, PastWorkImage
from .email import send_verification_email
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.auth.decorators import login_required


# This function routes the main home page
def Intro_home(request):

        return render(request, 'Discover/page2/index.html')

#This Function(view) routes to the onboarding page
@login_required
def onBoardings(request):
        return render(request, 'Discover/page2/onboardings.html')



# This view handles the tradespeople registation
@login_required
def tradesPeopleRegistration(request):
        user = request.user
        def safe_capitalize(val):
                return val.capitalize() if isinstance(val, str) and val else ""

        if request.method == "POST":
                form = TradespersonOnboardingForm2(request.POST, request.FILES)
                print(form.is_valid())
                print(form.errors)
                if form.is_valid():
                       
                        if Area.objects.filter(name__iexact=form.cleaned_data.get('work_areas')).exists():
                                area = Area.objects.get(name__iexact=form.cleaned_data.get('work_areas'))
                        else:
                                area = Area.objects.create(name=safe_capitalize(form.cleaned_data.get('work_areas')), city=form.cleaned_data.get('sub_location'))
                                area.save()

                        if TradeSpecialty.objects.filter(name__iexact=form.cleaned_data.get('trade_specialties')).exists():
                                specialty = TradeSpecialty.objects.get(name__iexact=form.cleaned_data.get('trade_specialties'))
                        else:
                                specialty = TradeSpecialty.objects.create(name=safe_capitalize(form.cleaned_data.get('trade_specialties')),\
                                                                           category=form.cleaned_data.get('trade_category'))
                                specialty.save()
        

                        print(form.cleaned_data)
                        print(request.FILES)
                        print(user)
                        Tradesperson = TradespersonProfile(
                                user=request.user,
                                first_name=safe_capitalize(form.cleaned_data.get('first_name')),
                                last_name=safe_capitalize(form.cleaned_data.get('last_name')),
                                other_names=safe_capitalize(form.cleaned_data.get('other_names')),
                                date_of_birth=form.cleaned_data.get('date_of_birth'),
                                gender=safe_capitalize(form.cleaned_data.get('gender')),
                                contact_number=form.cleaned_data.get('contact_number'),
                                contact_number2=form.cleaned_data.get('contact_number2'),
                                base_location=form.cleaned_data.get('base_location'),
                                sub_location=form.cleaned_data.get('sub_location'),
                                work_areas= area,
                                trade_category=form.cleaned_data.get('trade_category'),
                                bio=safe_capitalize(form.cleaned_data.get('bio')),
                        )

                        if 'profile_picture' in request.FILES:
                                Tradesperson.profile_picture = request.FILES['profile_picture']
                        Tradesperson.save()

                        Tradesperson.trade_specialties.add(specialty)

                        if form.cleaned_data.get('skills'):
                                Skills = form.cleaned_data.get('skills').split(",")
                                print(Skills)
                                for skill_name in Skills:
                                        skill_name = skill_name.strip()
                                        if skill_name:
                                                if TradeSkillTag.objects.filter(name__iexact=skill_name).exists():
                                                        skill = TradeSkillTag.objects.get(name__iexact=skill_name)
                                                else:
                                                        if form.cleaned_data.get('trade_category'):
                                                                skill = TradeSkillTag.objects.create(name=safe_capitalize(skill_name), category=form.cleaned_data.get('trade_category'))
                                                                skill.save()
                                                        else:
                                                                skill = TradeSkillTag.objects.create(name=safe_capitalize(skill_name), category=user.trade_category)
                                                                skill.save()
                                                        Tradesperson.skills.add(skill)

                        return redirect('Congratulations')
                else:
                        context = {
                                "form": form,
                                "specialties": TradeSpecialty.objects.all(),
                                "skills": TradeSkillTag.objects.all(),
                                "cities": City.objects.all(),
                                "areas": Area.objects.all(),
                        }
                        return render(request, "Discover/page2/tradespeopleRegister.html", context)
        else:
                form = TradespersonOnboardingForm2()
                print(user)

                # Send existing DB options for datalists
                context = {
                        "form": form,
                        "specialties": TradeSpecialty.objects.all(),
                        "skills": TradeSkillTag.objects.all(),
                        "cities": City.objects.all(),
                        "areas": Area.objects.all(),
                }
                return render(request, "Discover/page2/tradespeopleRegister.html", context)


# This function routes to the congratulationsPage
@login_required
def contratsPage(request):
       return render(request, 'Discover/page2/congratulationsPage.html')



# This function routes to the Get_started page
def get_started(request):

        return render(request, 'Discover/intro/GetStarted.html')

# This is a view for the mail will be sent notice page
@login_required
def email_notice(request):
       return render(request, 'account/emails_sent_msg.html')

# This function routes to the Sign Up page
def sign_up(request):
        if request.method == 'POST':
                form = WorkerfyUserForm(request.POST)
                if form.is_valid():
                        user = form.save(commit=False)
                        user.set_password(form.cleaned_data['password1'])
                        user.save()
                        #send_verification_email(user)
                        user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
                        if user is not None:
                                login(request, user, backend='Discover.backend_auths.WorkerfyUserBackend')
                                return redirect('Onboardings')
                        else:
                                form.add_error(None, 'Opps! Invalid login credentials.')

                else:
                        print(form.errors)
                        form.add_error(None, 'Authentication failed after registration.')
        else:
                form = WorkerfyUserForm()   

        return render(request, 'Discover/page2/registerPage.html', {'form': form})

# This function routes the login page
def login_view(request):
    next_url = request.GET.get('next') or request.POST.get('next') or 'discover'

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user, backend='Discover.backend_auths.WorkerfyUserBackend')

                if url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                    return redirect(next_url)
                return redirect('MainPAge')
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = LoginForm()

    return render(request, 'Discover/page2/loginPage.html', {'form': form})


# This view handles the email resend
def resend_email(request):
        user = request.user
        send_verification_email(user)
        return None

# This view leds to the verification page and handels the verification process
def verify_email(request): 
        if request.method == 'POST':
                
                if form.is_valid():
                        
                        try:
                                user = request.user
                        except user.DoesNotExist:
                                print(form.errors)
                                form.add_error(None, 'No user found')
                        
                        input_code = form.cleaned_data['code']
                        if str(input_code) == str(user.verification_code):
                                user.verified = True
                                user.save()
                                return redirect('verification_success')
                        else:
                                form.add_error(None, 'Verification was not successful')
                else:
                        form.add_error(None, 'Invaild code Entered')
        
        else:
                form = verificationByEmailForm()
                return render(request, 'Discover/into/verification_by_email.html', {'form': form})


# The following fuctions leads to the pages to learn more.
def home_learn(request):
        user = request.user

        if user:
                return render(request, 'Discover/main/GetS-Home.html', {"user": user})
        return render(request, 'Discover/main/GetS-Home.html')

def HIW_learn(request):

        return render(request, 'Discover/main/GetS-HiW.html')

def features_learn(request):

        return render(request, 'Discover/main/GetS-features.html')

def clients_learn(request):

        return render(request, 'Discover/main/GetS-ForC.html')

def tradespeople_learn(request):

        return render(request, 'Discover/main/GetS-forT.html')

def aboutUs_learn(request):

        return render(request, 'Discover/main/Gets-aboutUs.html')

def contactUS_learn(request):

        return render(request, 'Discover/main/GetS-ContactUs.html')


# This view handles the Profile page
def Profile_page_view(request):

        return render(request, 'Discover/main/profilePage.html')

# This view handles the notification page
def notifications_view(request):

        return render(request, 'Discover/main/notification.html')



# This view handles the Home learn page
def home_learn_view(request):

        return render(request, 'Discover/main/homeLearn.html')

# This view handles the 'Get sign up learn' page
def home_learn_login(request):

        return render(request, 'Discover/intro/get_startedLogin.html')

# This view handles the 'Create_As_C' page
def create_as_c(request):
        User_from_request = request.user

        UserC= WorkerfyUser.objects.filter(username=User_from_request.username).first()
        UserC.user_type = 'client'
        UserC.save()

        if request.method == "POST":
                form = ClientForm(request.POST, request.FILES)
                if form.is_valid():
                        USER = form.save(commit=False)
                        USER.user = User_from_request
                        USER.save()
                        return redirect('profile-page')
                else:
                        print('come here')
                        form.add_error(None, 'something went wrong')


        else:
                form = ClientForm()

        return render(request, 'Discover/intro/createAsC.html', {'form': form})

# This view handles the 'Create_As_T' page
def create_as_t(request):
        User_from_request = request.user

        UserC= WorkerfyUser.objects.filter(username=User_from_request.username).first()
        UserC.user_type = 'tradesperson'
        UserC.save()

        if request.method == "POST":
                form = TradespersonOnboardingForm2(request.POST, request.FILES)
                print(form.is_valid())
                if form.is_valid():
                        print(form.cleaned_data)
                        print(request.FILES)
                        print(request.user)
                        # Helper to safely capitalize or return empty string
                        def safe_capitalize(val):
                                return val.capitalize() if isinstance(val, str) and val else ""

                        Tradesperson = TradespersonProfile(
                                user=request.user,
                                first_name=safe_capitalize(form.cleaned_data.get('first_name')),
                                last_name=safe_capitalize(form.cleaned_data.get('last_name')),
                                other_names=safe_capitalize(form.cleaned_data.get('other_names')),
                                date_of_birth=form.cleaned_data.get('date_of_birth'),
                                gender=safe_capitalize(form.cleaned_data.get('gender')),
                                contact_number=form.cleaned_data.get('contact_number'),
                                contact_number2=form.cleaned_data.get('contact_number2'),
                                base_location=form.cleaned_data.get('base_location'),
                                sub_location=form.cleaned_data.get('sub_location'),
                                work_areas=form.cleaned_data.get('work_areas'),
                                trade_category=form.cleaned_data.get('trade_category'),
                                trade_specialties=safe_capitalize(form.cleaned_data.get('trade_specialties')),
                                skills=safe_capitalize(form.cleaned_data.get('skills')),                                                bio=safe_capitalize(form.cleaned_data.get('bio')),
                                        )
                        if 'profile_picture' in request.FILES:
                                Tradesperson.profile_picture = request.FILES['profile_picture']
                        Tradesperson.save()
                        return redirect('Congratulations')
                else:
                        # If form is invalid, render with errors and context
                        context = {
                                "form": form,
                                "specialties": TradeSpecialty.objects.all(),
                                "skills": TradeSkillTag.objects.all(),
                                "cities": City.objects.all(),
                                "areas": Area.objects.all(),
                                }
                        return render(request, "Discover/page2/tradespeopleRegister.html", context)
                return render(request, "Discover/page2/tradespeopleRegister.html", context)
        else:
                form = TradespersonOnboardingForm2()
                # Send existing DB options for datalists
                context = {
                        "form": form,
                        "specialties": TradeSpecialty.objects.all(),
                        "skills": TradeSkillTag.objects.all(),
                        "cities": City.objects.all(),
                        "areas": Area.objects.all(),
                        }
                return render(request, "Discover/page2/tradespeopleRegister.html", context)