from django.shortcuts import render, redirect
from .forms import TradespersonOnboardingForm, ProfileEditPageform, CertificateForm, PortfolioForm
from django.contrib.auth.decorators import login_required
from MainWorkerfy.models import TradespersonProfile, City, Area, TradeCategory, TradeSpecialty, TradeSkillTag, Region, Certificate, PortfolioItem
from django.contrib.auth.models import User
import json
import datetime

# Create your views here.

def forms(request):
    """
    This view renders the forms page.
    """
    if request.method == 'POST':
        # Handle form submission logic here if needed
        pass

    # Render the forms template
    form = TradespersonOnboardingForm()

    return render(request, 'main/forms.html', {'form': form})

# This view handles the Discover page
@login_required
def Main_page(request):
    print(request.user)

    Tradespeople = TradespersonProfile.objects.all()
    user = TradespersonProfile.objects.filter(user = request.user).first()

    print(user)

    context = {
        'Tradespeople': Tradespeople,
        'user': TradespersonProfile.objects.filter(user = request.user).first(),
    }

    return render(request, 'main/mainPageTradesperson.html', context)

@login_required
def TradespersonProfileEdit(request):
    def safe_capitalize(val):
        return val.capitalize() if isinstance(val, str) and val else ""

    if request.method == "POST":
        form = ProfileEditPageform(request.POST, request.FILES)
        certForm = CertificateForm(request.POST, request.FILES)
        portfolioForm = PortfolioForm(request.POST, request.FILES)


        if form.is_valid() and certForm.is_valid() and portfolioForm.is_valid():

            user = TradespersonProfile.objects.filter(user = request.user).first()
            print(form.cleaned_data)
            if form.cleaned_data.get('work_areas'):
                if Area.objects.filter(name__iexact=form.cleaned_data.get('work_areas')).exists():
                        area = Area.objects.get(name__iexact=form.cleaned_data.get('work_areas'))
                else:
                        area = Area.objects.create(name=safe_capitalize(form.cleaned_data.get('work_areas')), city=form.cleaned_data.get('sub_location'))
                        area.save()

            if form.cleaned_data.get('trade_specialties'):

                if TradeSpecialty.objects.filter(name__iexact=form.cleaned_data.get('trade_specialties')).exists():
                        specialty = TradeSpecialty.objects.get(name__iexact=form.cleaned_data.get('trade_specialties'))
                else:
                        if form.cleaned_data.get('trade_category'):
                            specialty = TradeSpecialty.objects.create(name=safe_capitalize(form.cleaned_data.get('trade_specialties')), category=form.cleaned_data.get('trade_category'))
                            specialty.save()
                        else:
                            specialty = TradeSpecialty.objects.create(name=safe_capitalize(form.cleaned_data.get('trade_specialties')), category=user.trade_category)
                            specialty.save()

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
                             user.skills.add(skill)
        
            


            for key, value in form.cleaned_data.items():
                 print(key, value)
                 
                 if value:
                    if key == 'work_areas':
                        user.work_areas.add(area)
                    elif key == 'trade_specialties':
                        user.trade_specialties.add(specialty)
                    elif key == 'social_links':
                         value = json.loads(value)
                         setattr(user, key, value)
                    elif key == 'working_areas':
                         covValue = []
                         
                         works = value.split("-- ")
                         print(works)
                         for work in works:  
                            value = json.loads(work)
                            covValue.append(value)
                         setattr(user, key, covValue)
                    elif key == 'education_schools':
                         covValue = []
                         
                         schools = value.split("-- ")
                         print(schools)
                         for school in schools:  
                            value = json.loads(school)
                            covValue.append(value)
                         setattr(user, key, covValue)
                    elif key == 'other_skills':
                         covValue = value.split(",")
                         setattr(user, key, covValue)
                    elif key == 'trade_category':
                         Trades = TradeCategory.objects.filter(name = "value").first()
                         user.trade_category = Trades
                    elif key == "experience_years":
                         setattr(user, key, int(value))
                    elif key == "skills":
                         continue
                    elif key == "date_of_birth":
                         print(type(value))
                         user.date_of_birth = value
                    else:
                         setattr(user, key, safe_capitalize(value))

                    
            user.save()

            # I will code entry for ares, specialization and skills here:


            # and end here


            # Next is the certificate entry

            if certForm.cleaned_data:
                                  
                 Cert = Certificate(tradesperson = user)

                 for key, value in certForm.cleaned_data.items():
                      #print(key,value)
                      setattr(Cert, key, value)

                 Cert.save()

            if portfolioForm.cleaned_data:
                 #print(portfolioForm.cleaned_data)

                 item = PortfolioItem(tradesperson = user)

                 for key, value in portfolioForm.cleaned_data.items():
                      print(key,value)
                      setattr(item, key, value)

                 item.save()


                 
                        

            print(user)

            print(user.first_name)

        return render(request, 'main/mainPageTradesperson.html')



    else:
        print(request.user)

        context = {
            'form': ProfileEditPageform(),
            'certForm': CertificateForm(),
            'portfolioForm': PortfolioForm(),
            'user': TradespersonProfile.objects.get(user = request.user),
        }
        print(context['user'].first_name)

        return render(request, 'main/TradespersonProfileEdit.html', context)